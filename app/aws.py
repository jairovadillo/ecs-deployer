import logging
import time

import boto3

import conf

client_sts = boto3.client('sts')

role_arn = "arn:aws:iam::{}:role/sso/{}".format(conf.ACCOUNT_ID, conf.ROLE_NAME)
assumed_role_object = client_sts.assume_role(
    RoleArn=role_arn,
    RoleSessionName="AssumeRoleSession"
)

credentials = assumed_role_object['Credentials']

client = boto3.client(
    'ecs',
    region_name='eu-west-1',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)


def register_task_definition(task_definition, family):
    response = client.register_task_definition(family=family,
                                               **task_definition)

    return response['taskDefinition']['revision']


def run_release_task(cluster, service, task_definition):
    service_description = client.describe_services(cluster=cluster, services=[service])

    network_configuration = service_description['services'][0]['networkConfiguration']

    response = client.run_task(cluster=cluster,
                               taskDefinition=task_definition,
                               launchType='FARGATE',
                               networkConfiguration=network_configuration)

    from pprint import pprint

    pprint(response)

    return response['tasks'][0]['taskArn']


def has_task_finished(cluster, task_arn, wait_seconds=5):
    task_description = client.describe_tasks(cluster=cluster, tasks=[task_arn])

    if task_description['tasks'][0]['lastStatus'] == 'STOPPED':
        exit_code = task_description['tasks'][0]['containers'][0]['exitCode']
        if exit_code == 0:
            return True
        else:
            raise Exception('Exit code not 0, got: {}'.format(exit_code))

    return False


def update_services(environment, project_name, revisions):
    for service_name, revision_number in revisions.items():
        cluster = "{}-21b".format(environment)
        service = "{}-{}".format(project_name, service_name)
        task_definition = "{}-{}-{}:{}".format(environment,
                                               project_name,
                                               service_name,
                                               revision_number)

        logging.info("Updating service {} with td: {}".format(service, task_definition))
        response = client.update_service(cluster=cluster,
                                         service=service,
                                         taskDefinition=task_definition)


def _parse_describe_services(aws_response):
    return {
        service['serviceName']: {
            deployment['status']: deployment['taskDefinition']
            for deployment in service['deployments']
        }
        for service in aws_response['services']
    }


def check_deployment(cluster, project_name, revisions):
    expeted_services_revision = {
        "{}-{}".format(project_name, service_name): revision_number
        for service_name, revision_number in revisions.items()
    }

    for i in range(0, 90):
        response = client.describe_services(cluster=cluster,
                                            services=list(expeted_services_revision.keys()))

        aws_services_status = _parse_describe_services(response)

        finished_services = []
        for service, revision_number in expeted_services_revision.items():
            # Check only one deployment is running
            logging.info("Checking service {} status...".format(service))
            if len(aws_services_status[service].keys()) == 1:
                aws_current_revision = aws_services_status[service]['PRIMARY'].split(':')[-1]

                if str(revision_number) == str(aws_current_revision):
                    logging.info("Service {} successfully updated with revision: {}".format(service, revision_number))
                    finished_services.append(service)
                else:
                    logging.info("Service {} is still running revision {}, needs rev. {}".format(service,
                                                                                                 aws_current_revision,
                                                                                                 revision_number))
            else:
                logging.info("Service {} has multiple deployments still running...".format(service))

        for s in finished_services:
            expeted_services_revision.pop(s)

            if len(expeted_services_revision.keys()) == 0:
                logging.info("All tasks successfully updated!")
                break

        time.sleep(10)

    logging.error("Timeout checking deployment! Services: {} not updated yet!".format(
        list(expeted_services_revision.keys())))
