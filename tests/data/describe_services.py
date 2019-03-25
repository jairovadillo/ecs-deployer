import datetime

from dateutil.tz import tzlocal

describe_services = {
    'ResponseMetadata': {
        'HTTPHeaders': {
            'content-length': '22738',
            'content-type': 'application/x-amz-json-1.1',
            'date': 'Thu, 28 Feb 2019 08:22:03 GMT',
            'x-amzn-requestid': 'edea6b56-3b31-11e9-a57e-27d9c7321367'},
        'HTTPStatusCode': 200,
        'RequestId': 'edea6b56-3b31-11e9-a57e-27d9c7321367',
        'RetryAttempts': 0
    },
    'failures': [],
    'services': [
        {
            'clusterArn': 'arn:aws:ecs:eu-west-1:708870636378:cluster/dev-21b',
            'createdAt': datetime.datetime(2018, 10, 15, 15, 29, 12, 908000, tzinfo=tzlocal()),
            'deploymentConfiguration': {
                'maximumPercent': 200,
                'minimumHealthyPercent': 100},
            'deployments': [
                {
                    'createdAt': datetime.datetime(2019, 2, 27, 16, 17, 11, 341000,
                                                   tzinfo=tzlocal()),
                    'desiredCount': 1,
                    'id': 'ecs-svc/9223370485570544464',
                    'launchType': 'FARGATE',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'assignPublicIp': 'DISABLED',
                            'securityGroups': ['sg-d39239aa'],
                            'subnets': ['subnet-07bb55375308cf8a2',
                                        'subnet-51ff1118',
                                        'subnet-0b230b53',
                                        'subnet-0a15fb6aa862c696b',
                                        'subnet-9a1bf7fd',
                                        'subnet-0e478470008d445d8']}},
                    'pendingCount': 0,
                    'platformVersion': '1.3.0',
                    'runningCount': 1,
                    'status': 'PRIMARY',
                    'taskDefinition': 'arn:aws:ecs:eu-west-1:708870636378:task-definition/dev-purchases-web:95',
                    'updatedAt': datetime.datetime(2019, 2, 27, 16, 19, 24, 223000,
                                                   tzinfo=tzlocal())}],
            'desiredCount': 1,
            'enableECSManagedTags': False,
            'events': [],
            'healthCheckGracePeriodSeconds': 100,
            'launchType': 'FARGATE',
            'loadBalancers': [
                {
                    'containerName': 'dev-purchases',
                    'containerPort': 8000,
                    'targetGroupArn': 'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160'
                }
            ],
            'networkConfiguration': {
                'awsvpcConfiguration': {
                    'assignPublicIp': 'DISABLED',
                    'securityGroups': ['sg-d39239aa'],
                    'subnets': [
                        'subnet-07bb55375308cf8a2',
                        'subnet-51ff1118',
                        'subnet-0b230b53',
                        'subnet-0a15fb6aa862c696b',
                        'subnet-9a1bf7fd',
                        'subnet-0e478470008d445d8']}},
            'pendingCount': 0,
            'placementConstraints': [],
            'placementStrategy': [],
            'platformVersion': 'LATEST',
            'propagateTags': 'NONE',
            'roleArn': 'arn:aws:iam::708870636378:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS',
            'runningCount': 1,
            'schedulingStrategy': 'REPLICA',
            'serviceArn': 'arn:aws:ecs:eu-west-1:708870636378:service/purchases-web',
            'serviceName': 'purchases-web',
            'serviceRegistries': [],
            'status': 'ACTIVE',
            'taskDefinition': 'arn:aws:ecs:eu-west-1:708870636378:task-definition/dev-purchases-web:95'
        },
        {
            'clusterArn': 'arn:aws:ecs:eu-west-1:708870636378:cluster/dev-21b',
            'createdAt': datetime.datetime(2018, 10, 15, 15, 29, 12, 908000, tzinfo=tzlocal()),
            'deploymentConfiguration': {
                'maximumPercent': 200,
                'minimumHealthyPercent': 100},
            'deployments': [
                {
                    'createdAt': datetime.datetime(2019, 2, 27, 16, 17, 11, 341000,
                                                   tzinfo=tzlocal()),
                    'desiredCount': 1,
                    'id': 'ecs-svc/9223370485570544464',
                    'launchType': 'FARGATE',
                    'networkConfiguration': {
                        'awsvpcConfiguration': {
                            'assignPublicIp': 'DISABLED',
                            'securityGroups': ['sg-d39239aa'],
                            'subnets': ['subnet-07bb55375308cf8a2',
                                        'subnet-51ff1118',
                                        'subnet-0b230b53',
                                        'subnet-0a15fb6aa862c696b',
                                        'subnet-9a1bf7fd',
                                        'subnet-0e478470008d445d8']}},
                    'pendingCount': 0,
                    'platformVersion': '1.3.0',
                    'runningCount': 1,
                    'status': 'PRIMARY',
                    'taskDefinition': 'arn:aws:ecs:eu-west-1:708870636378:task-definition/dev-purchases-default:145',
                    'updatedAt': datetime.datetime(2019, 2, 27, 16, 19, 24, 223000, tzinfo=tzlocal())}
            ],
            'desiredCount': 1,
            'enableECSManagedTags': False,
            'events': [],
            'healthCheckGracePeriodSeconds': 100,
            'launchType': 'FARGATE',
            'loadBalancers': [
                {
                    'containerName': 'dev-purchases',
                    'containerPort': 8000,
                    'targetGroupArn': 'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160'
                }
            ],
            'networkConfiguration': {
                'awsvpcConfiguration': {
                    'assignPublicIp': 'DISABLED',
                    'securityGroups': ['sg-d39239aa'],
                    'subnets': [
                        'subnet-07bb55375308cf8a2',
                        'subnet-51ff1118',
                        'subnet-0b230b53',
                        'subnet-0a15fb6aa862c696b',
                        'subnet-9a1bf7fd',
                        'subnet-0e478470008d445d8']}},
            'pendingCount': 0,
            'placementConstraints': [],
            'placementStrategy': [],
            'platformVersion': 'LATEST',
            'propagateTags': 'NONE',
            'roleArn': 'arn:aws:iam::708870636378:role/aws-service-role/ecs.amazonaws.com/AWSServiceRoleForECS',
            'runningCount': 1,
            'schedulingStrategy': 'REPLICA',
            'serviceArn': 'arn:aws:ecs:eu-west-1:708870636378:service/purchases-web',
            'serviceName': 'purchases-default',
            'serviceRegistries': [],
            'status': 'ACTIVE',
            'taskDefinition': 'arn:aws:ecs:eu-west-1:708870636378:task-definition/dev-purchases-default:145'
        }
    ]
}
