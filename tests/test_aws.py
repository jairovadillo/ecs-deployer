from unittest.mock import MagicMock

from ecs_deployer.aws import AWSWrapper


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


def test_describe_services():
    aws_client_mock = MagicMock()
    aws_client_mock.describe_services = _describe_services_mock

    aws = AWSWrapper(aws_client_mock)

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

