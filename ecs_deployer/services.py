import logging
import time
import yaml
from yaml import Loader

import conf
from aws import AWSWrapper
from task_definition import create_container_definition, create_task_definition

aws = AWSWrapper.build(conf.ACCOUNT_ID, conf.ROLE_NAME)


def read_procfile(procfile_path):
    try:
        f = open(procfile_path, 'r')
    except Exception as e:
        raise Exception("Cannot read procfile yaml!")
    else:
        return yaml.load(f, Loader=Loader)


def register_task_definitions(procfile_path, execution_role, environment, project_name, task_role,
                              ecr_path, secrets_manager=None):
    env_vars = secrets_manager.get_configuration_vars() if secrets_manager else {}
    procfile = read_procfile(procfile_path)

    revisions = {}
    for service_name, values in procfile.items():
        service_task_definition = create_task_definition(execution_role=execution_role,
                                                         cpu=values['cpu'],
                                                         memory=values['memory'],
                                                         task_role=task_role,
                                                         deployment_type=values.get('deployment-type', 'FARGATE'))

        container_definition = create_container_definition(env_vars,
                                                           environment,
                                                           project_name,
                                                           ecr_path=ecr_path,
                                                           container_name=service_name,
                                                           command=values['command'],
                                                           cpu=values['cpu'],
                                                           memory=values['memory'],
                                                           ports=values.get('ports'),
                                                           disable_logs=values.get('disable-logs', False),
                                                           region_name=conf.AWS_REGION_NAME)

        service_task_definition['containerDefinitions'].append(container_definition)

        family = "{}-{}-{}".format(environment,
                                   project_name,
                                   service_name)
        # TODO: handle errors
        revision = aws.register_task_definition(service_task_definition,
                                                family)

        revisions[service_name] = revision

    return revisions


def run_release_cmd(procfile_path, cluster, environment, project_name):
    procfile = read_procfile(procfile_path)

    if 'release' not in procfile.keys():
        return None

    service = "{}-web".format(project_name)
    task_definition = "{}-{}-release".format(environment,
                                             project_name)

    return aws.run_release_task(cluster, service, task_definition)


def wait_for_release_task(cluster, task_tracker):
    while not aws.has_task_finished(cluster, task_tracker):
        time.sleep(5)
        logging.info('Release task still in progress...')


def update_services(cluster, environment, project_name, revisions):
    aws.update_services(cluster, environment, project_name, revisions)


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
        raise Exception("timeout updating service task!")
