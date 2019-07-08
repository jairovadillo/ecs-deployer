from unittest.mock import MagicMock
from ecs_deployer.aws import AWSWrapper
from pytest import raises

def _describe_services_mock(cluster, services):
    services_list = []

    for s in services:
        services_list.append({
            'serviceName': s,
            'deployments': [
                {
                    'status': 'PRIMARY',
                    'taskDefinition': 'random-101'
                }
            ]
        })

    return {
        'services': services_list
    }


def _get_log_events_mock( logGroupName, logStreamName, startFromHead):
    s = {
        'events': [
            {
                'timestamp': 53452345235,
                'message': 'FATAL',
                'asd': '54543534'
            },
            {
                'timestamp': 53452345265,
                'message': 'action 1',
                'asd': '545463534'
            }
        ]
    }
    return s

def _describe_tasks_mock(cluster, tasks):
    message = {
            'tasks': [
                {
                    'lastStatus':'STOPPED',
                    'containers': [
                        {
                        'exitCode': 123,
                        'name': 'task1'

                        }
                    ]
                 }
            ]
        }

    return message


def test_describe_services():
    aws_client_ecs_mock = MagicMock()
    aws_client_ecs_mock.describe_services = _describe_services_mock

    aws_client_logs_mock = MagicMock()
    aws_client_logs_mock.get_log_events = _get_log_events_mock

    aws = AWSWrapper(aws_client_ecs_mock, aws_client_logs_mock)

    cluster_name = 'random-c'
    services = list(range(21))
    expected_response = {
        s: {
            'PRIMARY': 'random-101'
        }
        for s in services
    }

    response = aws.describe_services(cluster_name, services)

    assert response == expected_response

def test_release_task_failed():
    aws_client_ecs_mock = MagicMock()
    aws_client_ecs_mock.describe_services = _describe_services_mock
    aws_client_ecs_mock.describe_tasks = _describe_tasks_mock

    aws_client_logs_mock = MagicMock()
    aws_client_logs_mock.get_log_events = _get_log_events_mock

    aws = AWSWrapper(aws_client_ecs_mock, aws_client_logs_mock)
    cluster = 'c'
    task_arn = 'arn/task1'

    with raises(Exception):
        response = aws.has_task_finished(cluster=cluster, task_arn=task_arn)
        assert 'FATAL' in response

