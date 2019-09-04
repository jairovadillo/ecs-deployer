import json
import logging
import time

import conf
import yaml
from yaml import Loader
from aws import AWSWrapper
from task_definition import create_task_definition, create_container_definition
from vault import get_configuration_vars

aws = AWSWrapper.build(conf.ACCOUNT_ID, conf.ROLE_NAME)


def read_procfile(procfile_path):
    try:
        f = open(procfile_path, 'r')
    except Exception as e:
        raise Exception("Cannot read procfile yaml!")
    else:
        return yaml.load(f, Loader=Loader)


def read_yaml(yaml_path):
    try:
        f = open(yaml_path, 'r')
    except Exception as e:
        raise Exception("Cannot read yaml!", yaml_path)
    else:
        return yaml.load(f, Loader=Loader)


def register_task_definitions(procfile_path, vault_config, execution_role, environment, project_name, ecr_path):
    env_vars = get_configuration_vars(vault_config['host'],
                                      vault_config['token'],
                                      vault_config['path'])

    procfile = read_procfile(procfile_path)

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
                                                           memory=values['memory'],
                                                           ports=values.get('ports'))

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


def register_task_definitions_multi_container(container_definitions, vault_config, execution_role, environment,
                                              project_name, ecr_path):
    env_vars = get_configuration_vars(vault_config['host'],
                                      vault_config['token'],
                                      vault_config['path'])

    definitions = read_yaml(container_definitions)

    revisions = {}

    for service_name, values in definitions.items():

        values = replace_placeholder(values, env_vars, environment, ecr_path, execution_role)

        family = "{}-{}-{}".format(environment,
                                   project_name,
                                   service_name)

        revision = aws.register_task_definition(values,
                                                family)

        revisions[service_name] = revision

    return revisions


def replace_placeholder(dict, env_vars, environment, ecr_path, execution_role):
    for i in dict['containerDefinitions']:
        if i.get('environment', '') == '__ENV_VARS__':
            i['environment'] = env_vars

    str = json.dumps(dict)
    str = str.replace('__ENV__', environment)
    str = str.replace('__DOCKER_IMAGE__', ecr_path)
    str = str.replace('__EXEC_ROLE__', execution_role)
    modified_dict = json.loads(str)
    return modified_dict


def run_release_cmd(procfile_path, cluster, environment, project_name):
    procfile = read_procfile(procfile_path)

    if 'release' not in procfile.keys():
        return None

    service = "{}-web".format(project_name)
    task_definition = "{}-{}-release".format(environment,
                                             project_name)

    return aws.run_release_task(cluster, service, task_definition)


def run_release_cmd_multi_container(container_definitions, cluster, environment, project_name):
    container = read_yaml(container_definitions)

    if 'release' not in container.keys():
        return None

    service = "{}-release".format(project_name)
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

