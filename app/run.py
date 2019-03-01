import logging
import os
import time

import yaml

import aws
import conf
from task_definition import create_task_definition, create_container_definition
from vault import get_configuration_vars

logging.getLogger().setLevel(logging.INFO)


def read_procfile(procfile_name='procfile.yml'):
    try:
        path = './' + procfile_name
        path = os.path.join(os.getcwd(), path)
        f = open(path, 'r')
    except Exception as e:
        raise Exception("Cannot read procfile yaml!")
    else:
        return yaml.load(f)


def register_task_definitions(procfile_name, vault_config, execution_role, environment, project_name, ecr_path):
    env_vars = get_configuration_vars(vault_config['host'],
                                      vault_config['token'],
                                      vault_config['path'])

    procfile = read_procfile(procfile_name)

    revisions = {}

    for service_name, values in procfile.items():
        service_task_definition = create_task_definition(execution_role=execution_role,
                                                         cpu=values['cpu'],
                                                         memory=values['memory'])

        # for container in service
        container_definition = create_container_definition(env_vars,
                                                           environment,
                                                           project_name,
                                                           ecr_path=ecr_path,
                                                           container_name=service_name,
                                                           command=values['command'],
                                                           cpu=values['cpu'],
                                                           memory=values['memory'])

        service_task_definition['containerDefinitions'].append(container_definition)
        # end for

        family = "{}-{}-{}".format(environment,
                                   project_name,
                                   service_name)
        # TODO: handle errors
        revision = aws.register_task_definition(service_task_definition,
                                                family)

        revisions[service_name] = revision

    return revisions


def run_release_cmd(procfile_name, cluster, environment, project_name):
    procfile = read_procfile(procfile_name)

    if 'release' not in procfile.keys():
        return None

    service = "{}-web".format(project_name)
    task_definition = "{}-{}-release".format(environment,
                                             project_name)

    return aws.run_release_task(cluster, service, task_definition)


def wait_for_release_task(cluster, task_tracker):
    while not aws.has_task_finished(cluster, task_tracker):
        time.sleep(5)


def check_deployment(cluster, project_name, revisions):
    expeted_services_revision = {
        "{}-{}".format(project_name, service_name): revision_number
        for service_name, revision_number in revisions.items()
    }

    for i in range(0, 90):  # 90 * 10 = 10 minutes
        aws_services_status = aws.describe_services(cluster,
                                                    list(expeted_services_revision.keys()))

        finished_services = []
        for service, revision_number in expeted_services_revision.items():

            # Check only one deployment is running
            if len(aws_services_status[service].keys()) == 1:
                aws_current_revision = aws_services_status[service]['PRIMARY'].split(':')[-1]

                if str(revision_number) == str(aws_current_revision):
                    logging.info("Service {} successfully updated with revision: {}".format(service, revision_number))
                    finished_services.append(service)

        for s in finished_services:
            expeted_services_revision.pop(s)

        if len(expeted_services_revision.keys()) == 0:
            logging.info("All tasks successfully updated!")
            break

        logging.info("Services: {} are still updating tasks.".format(list(expeted_services_revision.keys())))
        time.sleep(10)
    else:
        logging.error("Timeout checking deployment! Services: {} not updated yet!".format(
            list(expeted_services_revision.keys())))


def main():
    logging.info("Registering task definitions")
    revisions = register_task_definitions(conf.PROCFILE_NAME,
                                          {
                                              'host': conf.VAULT_HOST,
                                              'token': conf.VAULT_TOKEN,
                                              'path': conf.VAULT_PATH
                                          },
                                          conf.EXECUTION_ROLE,
                                          conf.ENVIRONMENT,
                                          conf.PROJECT_NAME,
                                          conf.ECR_PATH)

    revisions.pop('release', None)

    logging.info("Running release command")
    task_tracker = run_release_cmd(conf.PROCFILE_NAME,
                                   conf.CLUSTER_NAME,
                                   conf.ENVIRONMENT,
                                   conf.PROJECT_NAME)

    if task_tracker:
        try:
            logging.info("Waiting for release task to finish ({})".format(task_tracker))
            wait_for_release_task(conf.CLUSTER_NAME, task_tracker)
        except Exception as e:
            logging.error("Error executing migrations: {}".format(e))
            raise e

    logging.info("Updating services")
    aws.update_services(conf.CLUSTER_NAME, conf.ENVIRONMENT, conf.PROJECT_NAME, revisions)

    logging.info("Checking deployment")
    check_deployment('{}-21b'.format(conf.ENVIRONMENT), conf.PROJECT_NAME, revisions)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(str(e))
        raise Exception(e)
