import logging

import boto3

client = boto3.client('ecs')


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

        logging.error("Updating service {} with td: {}".format(service, task_definition))
        client.update_service(cluster=cluster,
                              service=service,
                              taskDefinition=task_definition)
