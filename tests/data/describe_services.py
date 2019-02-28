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
            'events': [
                {'createdAt': datetime.datetime(2019, 2, 28, 4, 20, 45, 622000,
                                                tzinfo=tzlocal()),
                 'id': 'ac806f89-c3f1-43c7-9076-8c397e210b12',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 22, 20, 24, 742000,
                                                tzinfo=tzlocal()),
                 'id': '1df92a5d-69f2-4781-9c3c-79b3319a0a7a',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 20, 18, 225000,
                                                tzinfo=tzlocal()),
                 'id': '83416f63-3b33-47d1-ab42-5e0fd233dc6f',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 19, 55, 184000,
                                                tzinfo=tzlocal()),
                 'id': '8b6c81be-d521-4330-b43d-65f7730d4899',
                 'message': '(service purchases-web) has stopped 1 '
                            'running tasks: (task '
                            '41410b50-095d-4604-8841-0970889a8432).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 19, 35, 607000,
                                                tzinfo=tzlocal()),
                 'id': 'ce825e52-1f55-401f-a693-db33239e3738',
                 'message': '(service purchases-web) has begun '
                            'draining connections on 1 tasks.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 19, 35, 606000,
                                                tzinfo=tzlocal()),
                 'id': '845e8bc4-038e-441a-855d-56ba064c5b54',
                 'message': '(service purchases-web) deregistered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 18, 53, 609000,
                                                tzinfo=tzlocal()),
                 'id': 'af867a5f-4a2a-498e-845b-cd0897c7b81f',
                 'message': '(service purchases-web) registered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 18, 0, 60000,
                                                tzinfo=tzlocal()),
                 'id': '9201c143-eda4-4e44-b668-1a78c2162ac6',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'f030a961-c7f8-49ca-a000-5f7838f6c080).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 16, 29, 25000,
                                                tzinfo=tzlocal()),
                 'id': 'a3d9da41-b0f2-4925-8716-2595d8561593',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '19e107f2-62f3-4935-afc7-7b59e1d9e874).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 12, 29, 316000,
                                                tzinfo=tzlocal()),
                 'id': 'e13d123a-1b2e-4e2e-8f8d-b1a52bb712d7',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 12, 7, 341000,
                                                tzinfo=tzlocal()),
                 'id': '0e0ef0db-c644-4d1a-a5f5-45231539c851',
                 'message': '(service purchases-web) has stopped 1 '
                            'running tasks: (task '
                            'f1f50736-7102-47fa-b860-53d773921ff3).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 11, 45, 261000,
                                                tzinfo=tzlocal()),
                 'id': 'a0966476-1330-4baf-abdb-286702f236fb',
                 'message': '(service purchases-web) has begun '
                            'draining connections on 1 tasks.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 11, 45, 260000,
                                                tzinfo=tzlocal()),
                 'id': '7dbaa991-bc99-4df0-9d47-b365b554d0d4',
                 'message': '(service purchases-web) deregistered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 10, 56, 987000,
                                                tzinfo=tzlocal()),
                 'id': 'ee1cef57-2d44-449e-a679-27e064001b9f',
                 'message': '(service purchases-web) registered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 10, 5, 730000,
                                                tzinfo=tzlocal()),
                 'id': 'c233592c-5491-4540-8d27-8841f2ca0dc2',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '41410b50-095d-4604-8841-0970889a8432).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 3, 32, 303000,
                                                tzinfo=tzlocal()),
                 'id': 'e278c61a-0305-4bab-ac4a-3bad1b58b281',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 3, 8, 694000,
                                                tzinfo=tzlocal()),
                 'id': '30f63917-70bb-4829-99aa-2726bd2b79a4',
                 'message': '(service purchases-web) has stopped 1 '
                            'running tasks: (task '
                            '5413cf74-6231-4abc-aa42-e3eea6154399).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 2, 42, 237000,
                                                tzinfo=tzlocal()),
                 'id': '13a8a330-ffe5-4d90-8001-7607f75a547f',
                 'message': '(service purchases-web) has begun '
                            'draining connections on 1 tasks.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 2, 42, 236000,
                                                tzinfo=tzlocal()),
                 'id': '39502763-d3a8-4492-a149-ddae3d8cdc86',
                 'message': '(service purchases-web) deregistered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 2, 2, 123000,
                                                tzinfo=tzlocal()),
                 'id': 'e088d72d-cd2b-433d-966c-3e645b1fffbe',
                 'message': '(service purchases-web) registered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 1, 9, 670000,
                                                tzinfo=tzlocal()),
                 'id': 'ab622543-9988-4fa4-9a7d-7cb596d7acec',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'f1f50736-7102-47fa-b860-53d773921ff3).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 52, 1, 390000,
                                                tzinfo=tzlocal()),
                 'id': '17a0a07e-87ba-4072-81f5-7c34c6e87602',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 51, 6, 471000,
                                                tzinfo=tzlocal()),
                 'id': '47f47d34-cd74-4da8-986f-c7cc79edf548',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'f48b0da6-07cb-4e3b-b9f1-0af425040940).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 36, 25, 501000,
                                                tzinfo=tzlocal()),
                 'id': 'a5ffda23-7b1e-41eb-933e-a7ca72620efa',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 35, 34, 536000,
                                                tzinfo=tzlocal()),
                 'id': 'd21ca257-4154-40e7-9554-ad2365194613',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'e5e0af94-416f-42b4-880e-36c513d29fce).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 21, 0, 243000,
                                                tzinfo=tzlocal()),
                 'id': '0d60add2-f743-4a1f-922d-a477384ccb23',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 20, 6, 298000,
                                                tzinfo=tzlocal()),
                 'id': 'f4f044b3-b186-4bda-934d-fe257b76e1ab',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '5fd26788-2382-42ff-88de-988cb5e94aee).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 4, 54, 426000,
                                                tzinfo=tzlocal()),
                 'id': '9c9ec53a-0b21-4955-af8d-cd08905d3a78',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 3, 56, 593000,
                                                tzinfo=tzlocal()),
                 'id': '076a0602-6227-43e2-8282-8c7e40ed24e5',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'bedd35de-ddc4-428b-a6ff-68341e5a7ba8).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 48, 36, 84000,
                                                tzinfo=tzlocal()),
                 'id': '206ea6e8-6f3f-4832-ae72-f97bb8bb3749',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 47, 31, 788000,
                                                tzinfo=tzlocal()),
                 'id': 'e1ff98b9-c561-4798-9c8b-4e53c6b20b52',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '04969366-e00e-4084-90b2-cd4ee2cb8c5a).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 32, 50, 602000,
                                                tzinfo=tzlocal()),
                 'id': '1170a9ed-5bc1-4f12-82ad-8d9837bc1745',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 31, 48, 765000,
                                                tzinfo=tzlocal()),
                 'id': 'fdc029bd-c3e5-4aef-bbb8-f468e5cf2beb',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3cdb8fac-819f-4c93-8bda-7dc1ea59dcfe).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 16, 14, 208000,
                                                tzinfo=tzlocal()),
                 'id': '99d38019-b92a-4c65-90c3-89f93694a388',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 15, 15, 197000,
                                                tzinfo=tzlocal()),
                 'id': '5036f2bb-1b96-40c4-85f8-9e5859924729',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3f1c1d7b-e902-4c26-8c49-7f4317870302).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 0, 12, 432000,
                                                tzinfo=tzlocal()),
                 'id': '1ec1504a-a6cc-4eed-82e5-0597adb23d83',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 59, 13, 778000,
                                                tzinfo=tzlocal()),
                 'id': '0ed1c08f-5349-4355-a3da-e4284b1e1064',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '27263934-0506-43b2-b571-9270bc22449c).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 43, 39, 749000,
                                                tzinfo=tzlocal()),
                 'id': '5f127a87-108a-4785-a754-966c979f32d6',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 42, 39, 457000,
                                                tzinfo=tzlocal()),
                 'id': '64bae7ed-3e5e-40f7-984a-6b2e13ffbb73',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '11c2a19c-e2d6-4456-9319-4bc9fa54bd97).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 26, 57, 109000,
                                                tzinfo=tzlocal()),
                 'id': 'e48f86a0-29c6-4a1b-873f-0483764dfed4',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 25, 51, 62000,
                                                tzinfo=tzlocal()),
                 'id': 'e4c72cbc-144c-4f52-ba44-9116ba652f5b',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '85822508-927e-4e84-b0c0-c036649c6a40).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 11, 14, 363000,
                                                tzinfo=tzlocal()),
                 'id': 'bb798cd9-f7cc-4781-b94a-6eedfdf3c24b',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 10, 12, 891000,
                                                tzinfo=tzlocal()),
                 'id': '6bb4484b-e3e1-4872-b183-94b2695266b0',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3cabb602-ce3a-4fff-80c8-8083a7bb8ec7).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 55, 18, 304000,
                                                tzinfo=tzlocal()),
                 'id': '3b2941e5-411f-404a-8e99-7266e055d771',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 54, 7, 511000,
                                                tzinfo=tzlocal()),
                 'id': '86577725-c78d-4498-b21f-da497198e9b9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'd48973d8-633b-4e80-a52d-c4dd356b0625).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 38, 58, 353000,
                                                tzinfo=tzlocal()),
                 'id': 'a05854b5-be11-448a-84ff-f4042312305b',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 38, 9, 350000,
                                                tzinfo=tzlocal()),
                 'id': '7c988f47-2f43-4577-92ca-5339b816eb1a',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3d285dc0-85f0-492a-a16e-f8accff8d1ee).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 22, 34, 496000,
                                                tzinfo=tzlocal()),
                 'id': '80e5716a-d872-44ac-adcb-e5ceed1f844c',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 21, 42, 288000,
                                                tzinfo=tzlocal()),
                 'id': 'e0dc5d8a-87f1-4784-bde5-7478b6f41f11',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '5629dfc3-42ac-4047-8606-c04ff1c7b2aa).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 6, 39, 180000,
                                                tzinfo=tzlocal()),
                 'id': 'dfbd7f28-182d-4274-bb3f-f4a85ce3cbae',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 5, 37, 624000,
                                                tzinfo=tzlocal()),
                 'id': 'af2d0e6f-7270-4abd-ac88-aaa800f53411',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '010ab0f4-7b04-4a51-9a8c-b04ece4f4ca2).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 50, 53, 320000,
                                                tzinfo=tzlocal()),
                 'id': 'd2b88f08-637a-4e0c-9daa-962968656286',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 49, 55, 86000,
                                                tzinfo=tzlocal()),
                 'id': '7bc380f9-ba57-4f1b-9d62-b1eeb631fdcd',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '218933ee-0c07-4922-b34c-917108127354).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 34, 29, 131000,
                                                tzinfo=tzlocal()),
                 'id': 'faf669bd-ac54-454d-87a1-0b5c8997015a',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 33, 28, 423000,
                                                tzinfo=tzlocal()),
                 'id': 'cf73c313-d781-46cc-97e7-95db1f851019',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'db56c31e-9be1-42c3-bccc-8b57c13a1fed).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 19, 1, 941000,
                                                tzinfo=tzlocal()),
                 'id': '9b1b14c7-eedf-4026-baaf-69145e52a0c0',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 18, 3, 277000,
                                                tzinfo=tzlocal()),
                 'id': '31fd585f-5a1e-4a00-9318-34882d65e55d',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '4ffe47d1-d41a-44cf-aae9-7dca54e485f7).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 3, 0, 254000,
                                                tzinfo=tzlocal()),
                 'id': 'ff96de19-62a1-46a2-936d-351992a6f82b',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 1, 59, 214000,
                                                tzinfo=tzlocal()),
                 'id': '54cd9e8a-6a8a-4159-914b-6a960d6a052c',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'e0685d44-0c7b-43e6-bf39-4a65660eba9d).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 46, 37, 630000,
                                                tzinfo=tzlocal()),
                 'id': '573f96c6-b609-4a51-93ef-89802311aa2e',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 45, 37, 473000,
                                                tzinfo=tzlocal()),
                 'id': '29953dde-c764-45ed-ae19-aaff58b819fa',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '9d96c10e-5665-4958-aa7e-c9afb9a986eb).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 30, 17, 66000,
                                                tzinfo=tzlocal()),
                 'id': '59bdc4cb-b8c1-49fa-ad4c-a6fdb70ceb59',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 29, 16, 818000,
                                                tzinfo=tzlocal()),
                 'id': 'a05ef278-6452-45b3-821f-c4ed3a9b6618',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '1dea1727-11ca-4faa-9746-971d36eeccd1).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 14, 35, 868000,
                                                tzinfo=tzlocal()),
                 'id': '9cf93512-d7ad-4d4f-953d-9124c27e7d21',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 13, 36, 897000,
                                                tzinfo=tzlocal()),
                 'id': '873fbace-aa1a-41cb-87ba-8bc7443a35c9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '6eeec8b9-7414-486f-b3f3-cff562069de9).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 58, 5, 741000,
                                                tzinfo=tzlocal()),
                 'id': '7f92c2cc-be76-4f8e-a230-fdc00084048d',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 57, 6, 707000,
                                                tzinfo=tzlocal()),
                 'id': 'fffbf538-9698-40d5-b998-09f485d87059',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'c12bde63-05c7-4969-8f12-b0736f6ccd4d).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 41, 33, 908000,
                                                tzinfo=tzlocal()),
                 'id': 'e6bb40cb-4e4c-4503-9745-6602843d1ab4',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 40, 29, 578000,
                                                tzinfo=tzlocal()),
                 'id': '87a56682-4aa6-4db7-9e50-7efe4f103c4b',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '5b4d8b6c-c3af-4acb-926a-56e22bb52651).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 26, 7, 814000,
                                                tzinfo=tzlocal()),
                 'id': 'e8adf896-a0ad-451d-8ec9-ed6bac008246',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 25, 12, 278000,
                                                tzinfo=tzlocal()),
                 'id': 'bd47293b-5227-45a4-ae60-ebdf5e60e3d9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '6e25ad64-1d51-4653-ab72-51fe58e24b11).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 10, 18, 328000,
                                                tzinfo=tzlocal()),
                 'id': 'ca6f88a6-e439-4e81-9a21-39176a4c9aa5',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 9, 17, 716000,
                                                tzinfo=tzlocal()),
                 'id': 'eb7d6bd4-6b8f-42e6-831a-53e14c9768f0',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'c01d9e9f-24f6-4e93-b491-7f425f8eaef2).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 53, 33, 893000,
                                                tzinfo=tzlocal()),
                 'id': 'ad29f482-ba09-45ff-a0a6-40a4f09c4bda',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 52, 41, 173000,
                                                tzinfo=tzlocal()),
                 'id': '67d81659-6270-434c-a02d-663ac7825a84',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '394dfbf3-9bee-4361-b30a-2fa979d76518).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 36, 54, 630000,
                                                tzinfo=tzlocal()),
                 'id': '386ab757-054c-4c16-b38d-5c3b7cba20ff',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 35, 56, 681000,
                                                tzinfo=tzlocal()),
                 'id': '2e8f2752-8156-469a-aaba-c3794554d92b',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '574b0ff1-2593-4a82-ad48-f4ddd05a3d36).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 20, 13, 103000,
                                                tzinfo=tzlocal()),
                 'id': '11d4a24b-cbfd-4ab1-9696-c3c5e79f15f7',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 19, 16, 56000,
                                                tzinfo=tzlocal()),
                 'id': '0b40b2f6-a256-46ec-8ef5-ceb6bcaa38c9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'bb60b8df-6c6d-46e6-bd3b-2ac4bffc4e92).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 4, 48, 512000,
                                                tzinfo=tzlocal()),
                 'id': 'e28c7b11-f0c1-4ad4-9b27-20ef9da73031',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 3, 47, 912000,
                                                tzinfo=tzlocal()),
                 'id': '802d451d-bb74-4f18-9505-f5f3dea6ecd9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '59235234-06b1-4c8e-b992-395e6c703dca).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 49, 4, 585000,
                                                tzinfo=tzlocal()),
                 'id': 'f2bac145-51b0-44f6-84f4-95542fc8f540',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 48, 9, 346000,
                                                tzinfo=tzlocal()),
                 'id': '97c50e63-d1f3-4143-ba54-92ae94ad8673',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'ca5832dc-bffb-4f2b-92b5-4158a64ca11b).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 33, 26, 137000,
                                                tzinfo=tzlocal()),
                 'id': 'ccddc586-f40a-4f6a-80ab-73a78fbd31b9',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 32, 27, 571000,
                                                tzinfo=tzlocal()),
                 'id': 'ee7016ea-7580-4a39-928a-eda1ef31fcd1',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '46151cc3-3acc-49d8-882b-034d66579933).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 17, 8, 367000,
                                                tzinfo=tzlocal()),
                 'id': '2c5e6030-4a1a-47f9-8f52-ec36b4c09e05',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 16, 9, 859000,
                                                tzinfo=tzlocal()),
                 'id': '1d75fcc7-2e00-4453-8da4-d0a9b1ab938f',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '6af1376f-cf74-479f-ac86-7f8ea7717e77).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 1, 8, 156000,
                                                tzinfo=tzlocal()),
                 'id': 'f3df9de3-8bbb-498c-b4a5-fc54ae9b8d95',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 0, 10, 519000,
                                                tzinfo=tzlocal()),
                 'id': '51ad0db5-33c9-4c43-9104-5304cf14bc79',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '8f0e9af1-7952-405e-8194-21065b509ca6).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 45, 26, 935000,
                                                tzinfo=tzlocal()),
                 'id': '341ac3bf-03ce-4f42-8607-fb11596215e3',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 44, 29, 750000,
                                                tzinfo=tzlocal()),
                 'id': '67a68854-ba81-43e2-b269-b05aaf150877',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '561aae47-2f2a-4351-bd23-db4329a63430).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 29, 4, 234000,
                                                tzinfo=tzlocal()),
                 'id': '075b5676-44fc-4259-bb73-c82746fdd1ca',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 28, 4, 565000,
                                                tzinfo=tzlocal()),
                 'id': 'c252ad94-7bcc-4bf8-8825-1c9a908ed8a3',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'b4bd9f25-4c91-4f99-87e6-6354d5cb6a52).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 13, 35, 375000,
                                                tzinfo=tzlocal()),
                 'id': '5c5d939e-e462-4728-abf8-182585c8c7b4',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {
                    'createdAt': datetime.datetime(2019, 2, 27, 2, 12, 37, 858000,
                                                   tzinfo=tzlocal()),
                    'id': 'a3e37cd5-3a1f-4d59-b99a-744a456ea347',
                    'message': '(service purchases-web) has started 1 '
                               'tasks: (task '
                               'a55604ef-5b32-4e97-8e4f-972142fef058).'
                }
            ],
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
            'events': [
                {'createdAt': datetime.datetime(2019, 2, 28, 4, 20, 45, 622000,
                                                tzinfo=tzlocal()),
                 'id': 'ac806f89-c3f1-43c7-9076-8c397e210b12',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 22, 20, 24, 742000,
                                                tzinfo=tzlocal()),
                 'id': '1df92a5d-69f2-4781-9c3c-79b3319a0a7a',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 20, 18, 225000,
                                                tzinfo=tzlocal()),
                 'id': '83416f63-3b33-47d1-ab42-5e0fd233dc6f',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 19, 55, 184000,
                                                tzinfo=tzlocal()),
                 'id': '8b6c81be-d521-4330-b43d-65f7730d4899',
                 'message': '(service purchases-web) has stopped 1 '
                            'running tasks: (task '
                            '41410b50-095d-4604-8841-0970889a8432).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 19, 35, 607000,
                                                tzinfo=tzlocal()),
                 'id': 'ce825e52-1f55-401f-a693-db33239e3738',
                 'message': '(service purchases-web) has begun '
                            'draining connections on 1 tasks.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 19, 35, 606000,
                                                tzinfo=tzlocal()),
                 'id': '845e8bc4-038e-441a-855d-56ba064c5b54',
                 'message': '(service purchases-web) deregistered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 18, 53, 609000,
                                                tzinfo=tzlocal()),
                 'id': 'af867a5f-4a2a-498e-845b-cd0897c7b81f',
                 'message': '(service purchases-web) registered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 18, 0, 60000,
                                                tzinfo=tzlocal()),
                 'id': '9201c143-eda4-4e44-b668-1a78c2162ac6',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'f030a961-c7f8-49ca-a000-5f7838f6c080).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 16, 29, 25000,
                                                tzinfo=tzlocal()),
                 'id': 'a3d9da41-b0f2-4925-8716-2595d8561593',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '19e107f2-62f3-4935-afc7-7b59e1d9e874).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 12, 29, 316000,
                                                tzinfo=tzlocal()),
                 'id': 'e13d123a-1b2e-4e2e-8f8d-b1a52bb712d7',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 12, 7, 341000,
                                                tzinfo=tzlocal()),
                 'id': '0e0ef0db-c644-4d1a-a5f5-45231539c851',
                 'message': '(service purchases-web) has stopped 1 '
                            'running tasks: (task '
                            'f1f50736-7102-47fa-b860-53d773921ff3).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 11, 45, 261000,
                                                tzinfo=tzlocal()),
                 'id': 'a0966476-1330-4baf-abdb-286702f236fb',
                 'message': '(service purchases-web) has begun '
                            'draining connections on 1 tasks.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 11, 45, 260000,
                                                tzinfo=tzlocal()),
                 'id': '7dbaa991-bc99-4df0-9d47-b365b554d0d4',
                 'message': '(service purchases-web) deregistered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 10, 56, 987000,
                                                tzinfo=tzlocal()),
                 'id': 'ee1cef57-2d44-449e-a679-27e064001b9f',
                 'message': '(service purchases-web) registered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 16, 10, 5, 730000,
                                                tzinfo=tzlocal()),
                 'id': 'c233592c-5491-4540-8d27-8841f2ca0dc2',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '41410b50-095d-4604-8841-0970889a8432).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 3, 32, 303000,
                                                tzinfo=tzlocal()),
                 'id': 'e278c61a-0305-4bab-ac4a-3bad1b58b281',
                 'message': '(service purchases-web) has reached a '
                            'steady state.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 3, 8, 694000,
                                                tzinfo=tzlocal()),
                 'id': '30f63917-70bb-4829-99aa-2726bd2b79a4',
                 'message': '(service purchases-web) has stopped 1 '
                            'running tasks: (task '
                            '5413cf74-6231-4abc-aa42-e3eea6154399).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 2, 42, 237000,
                                                tzinfo=tzlocal()),
                 'id': '13a8a330-ffe5-4d90-8001-7607f75a547f',
                 'message': '(service purchases-web) has begun '
                            'draining connections on 1 tasks.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 2, 42, 236000,
                                                tzinfo=tzlocal()),
                 'id': '39502763-d3a8-4492-a149-ddae3d8cdc86',
                 'message': '(service purchases-web) deregistered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 2, 2, 123000,
                                                tzinfo=tzlocal()),
                 'id': 'e088d72d-cd2b-433d-966c-3e645b1fffbe',
                 'message': '(service purchases-web) registered 1 '
                            'targets in (target-group '
                            'arn:aws:elasticloadbalancing:eu-west-1:708870636378:targetgroup/dev-purchases-tg/be2977fa0c10a160)'},
                {'createdAt': datetime.datetime(2019, 2, 27, 12, 1, 9, 670000,
                                                tzinfo=tzlocal()),
                 'id': 'ab622543-9988-4fa4-9a7d-7cb596d7acec',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'f1f50736-7102-47fa-b860-53d773921ff3).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 52, 1, 390000,
                                                tzinfo=tzlocal()),
                 'id': '17a0a07e-87ba-4072-81f5-7c34c6e87602',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 51, 6, 471000,
                                                tzinfo=tzlocal()),
                 'id': '47f47d34-cd74-4da8-986f-c7cc79edf548',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'f48b0da6-07cb-4e3b-b9f1-0af425040940).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 36, 25, 501000,
                                                tzinfo=tzlocal()),
                 'id': 'a5ffda23-7b1e-41eb-933e-a7ca72620efa',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 35, 34, 536000,
                                                tzinfo=tzlocal()),
                 'id': 'd21ca257-4154-40e7-9554-ad2365194613',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'e5e0af94-416f-42b4-880e-36c513d29fce).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 21, 0, 243000,
                                                tzinfo=tzlocal()),
                 'id': '0d60add2-f743-4a1f-922d-a477384ccb23',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 20, 6, 298000,
                                                tzinfo=tzlocal()),
                 'id': 'f4f044b3-b186-4bda-934d-fe257b76e1ab',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '5fd26788-2382-42ff-88de-988cb5e94aee).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 4, 54, 426000,
                                                tzinfo=tzlocal()),
                 'id': '9c9ec53a-0b21-4955-af8d-cd08905d3a78',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 11, 3, 56, 593000,
                                                tzinfo=tzlocal()),
                 'id': '076a0602-6227-43e2-8282-8c7e40ed24e5',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'bedd35de-ddc4-428b-a6ff-68341e5a7ba8).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 48, 36, 84000,
                                                tzinfo=tzlocal()),
                 'id': '206ea6e8-6f3f-4832-ae72-f97bb8bb3749',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 47, 31, 788000,
                                                tzinfo=tzlocal()),
                 'id': 'e1ff98b9-c561-4798-9c8b-4e53c6b20b52',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '04969366-e00e-4084-90b2-cd4ee2cb8c5a).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 32, 50, 602000,
                                                tzinfo=tzlocal()),
                 'id': '1170a9ed-5bc1-4f12-82ad-8d9837bc1745',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 31, 48, 765000,
                                                tzinfo=tzlocal()),
                 'id': 'fdc029bd-c3e5-4aef-bbb8-f468e5cf2beb',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3cdb8fac-819f-4c93-8bda-7dc1ea59dcfe).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 16, 14, 208000,
                                                tzinfo=tzlocal()),
                 'id': '99d38019-b92a-4c65-90c3-89f93694a388',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 15, 15, 197000,
                                                tzinfo=tzlocal()),
                 'id': '5036f2bb-1b96-40c4-85f8-9e5859924729',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3f1c1d7b-e902-4c26-8c49-7f4317870302).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 10, 0, 12, 432000,
                                                tzinfo=tzlocal()),
                 'id': '1ec1504a-a6cc-4eed-82e5-0597adb23d83',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 59, 13, 778000,
                                                tzinfo=tzlocal()),
                 'id': '0ed1c08f-5349-4355-a3da-e4284b1e1064',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '27263934-0506-43b2-b571-9270bc22449c).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 43, 39, 749000,
                                                tzinfo=tzlocal()),
                 'id': '5f127a87-108a-4785-a754-966c979f32d6',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 42, 39, 457000,
                                                tzinfo=tzlocal()),
                 'id': '64bae7ed-3e5e-40f7-984a-6b2e13ffbb73',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '11c2a19c-e2d6-4456-9319-4bc9fa54bd97).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 26, 57, 109000,
                                                tzinfo=tzlocal()),
                 'id': 'e48f86a0-29c6-4a1b-873f-0483764dfed4',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 25, 51, 62000,
                                                tzinfo=tzlocal()),
                 'id': 'e4c72cbc-144c-4f52-ba44-9116ba652f5b',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '85822508-927e-4e84-b0c0-c036649c6a40).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 11, 14, 363000,
                                                tzinfo=tzlocal()),
                 'id': 'bb798cd9-f7cc-4781-b94a-6eedfdf3c24b',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 9, 10, 12, 891000,
                                                tzinfo=tzlocal()),
                 'id': '6bb4484b-e3e1-4872-b183-94b2695266b0',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3cabb602-ce3a-4fff-80c8-8083a7bb8ec7).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 55, 18, 304000,
                                                tzinfo=tzlocal()),
                 'id': '3b2941e5-411f-404a-8e99-7266e055d771',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 54, 7, 511000,
                                                tzinfo=tzlocal()),
                 'id': '86577725-c78d-4498-b21f-da497198e9b9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'd48973d8-633b-4e80-a52d-c4dd356b0625).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 38, 58, 353000,
                                                tzinfo=tzlocal()),
                 'id': 'a05854b5-be11-448a-84ff-f4042312305b',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 38, 9, 350000,
                                                tzinfo=tzlocal()),
                 'id': '7c988f47-2f43-4577-92ca-5339b816eb1a',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '3d285dc0-85f0-492a-a16e-f8accff8d1ee).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 22, 34, 496000,
                                                tzinfo=tzlocal()),
                 'id': '80e5716a-d872-44ac-adcb-e5ceed1f844c',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 21, 42, 288000,
                                                tzinfo=tzlocal()),
                 'id': 'e0dc5d8a-87f1-4784-bde5-7478b6f41f11',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '5629dfc3-42ac-4047-8606-c04ff1c7b2aa).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 6, 39, 180000,
                                                tzinfo=tzlocal()),
                 'id': 'dfbd7f28-182d-4274-bb3f-f4a85ce3cbae',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 8, 5, 37, 624000,
                                                tzinfo=tzlocal()),
                 'id': 'af2d0e6f-7270-4abd-ac88-aaa800f53411',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '010ab0f4-7b04-4a51-9a8c-b04ece4f4ca2).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 50, 53, 320000,
                                                tzinfo=tzlocal()),
                 'id': 'd2b88f08-637a-4e0c-9daa-962968656286',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 49, 55, 86000,
                                                tzinfo=tzlocal()),
                 'id': '7bc380f9-ba57-4f1b-9d62-b1eeb631fdcd',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '218933ee-0c07-4922-b34c-917108127354).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 34, 29, 131000,
                                                tzinfo=tzlocal()),
                 'id': 'faf669bd-ac54-454d-87a1-0b5c8997015a',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 33, 28, 423000,
                                                tzinfo=tzlocal()),
                 'id': 'cf73c313-d781-46cc-97e7-95db1f851019',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'db56c31e-9be1-42c3-bccc-8b57c13a1fed).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 19, 1, 941000,
                                                tzinfo=tzlocal()),
                 'id': '9b1b14c7-eedf-4026-baaf-69145e52a0c0',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 18, 3, 277000,
                                                tzinfo=tzlocal()),
                 'id': '31fd585f-5a1e-4a00-9318-34882d65e55d',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '4ffe47d1-d41a-44cf-aae9-7dca54e485f7).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 3, 0, 254000,
                                                tzinfo=tzlocal()),
                 'id': 'ff96de19-62a1-46a2-936d-351992a6f82b',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 7, 1, 59, 214000,
                                                tzinfo=tzlocal()),
                 'id': '54cd9e8a-6a8a-4159-914b-6a960d6a052c',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'e0685d44-0c7b-43e6-bf39-4a65660eba9d).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 46, 37, 630000,
                                                tzinfo=tzlocal()),
                 'id': '573f96c6-b609-4a51-93ef-89802311aa2e',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 45, 37, 473000,
                                                tzinfo=tzlocal()),
                 'id': '29953dde-c764-45ed-ae19-aaff58b819fa',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '9d96c10e-5665-4958-aa7e-c9afb9a986eb).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 30, 17, 66000,
                                                tzinfo=tzlocal()),
                 'id': '59bdc4cb-b8c1-49fa-ad4c-a6fdb70ceb59',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 29, 16, 818000,
                                                tzinfo=tzlocal()),
                 'id': 'a05ef278-6452-45b3-821f-c4ed3a9b6618',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '1dea1727-11ca-4faa-9746-971d36eeccd1).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 14, 35, 868000,
                                                tzinfo=tzlocal()),
                 'id': '9cf93512-d7ad-4d4f-953d-9124c27e7d21',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 6, 13, 36, 897000,
                                                tzinfo=tzlocal()),
                 'id': '873fbace-aa1a-41cb-87ba-8bc7443a35c9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '6eeec8b9-7414-486f-b3f3-cff562069de9).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 58, 5, 741000,
                                                tzinfo=tzlocal()),
                 'id': '7f92c2cc-be76-4f8e-a230-fdc00084048d',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 57, 6, 707000,
                                                tzinfo=tzlocal()),
                 'id': 'fffbf538-9698-40d5-b998-09f485d87059',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'c12bde63-05c7-4969-8f12-b0736f6ccd4d).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 41, 33, 908000,
                                                tzinfo=tzlocal()),
                 'id': 'e6bb40cb-4e4c-4503-9745-6602843d1ab4',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 40, 29, 578000,
                                                tzinfo=tzlocal()),
                 'id': '87a56682-4aa6-4db7-9e50-7efe4f103c4b',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '5b4d8b6c-c3af-4acb-926a-56e22bb52651).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 26, 7, 814000,
                                                tzinfo=tzlocal()),
                 'id': 'e8adf896-a0ad-451d-8ec9-ed6bac008246',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 25, 12, 278000,
                                                tzinfo=tzlocal()),
                 'id': 'bd47293b-5227-45a4-ae60-ebdf5e60e3d9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '6e25ad64-1d51-4653-ab72-51fe58e24b11).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 10, 18, 328000,
                                                tzinfo=tzlocal()),
                 'id': 'ca6f88a6-e439-4e81-9a21-39176a4c9aa5',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 5, 9, 17, 716000,
                                                tzinfo=tzlocal()),
                 'id': 'eb7d6bd4-6b8f-42e6-831a-53e14c9768f0',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'c01d9e9f-24f6-4e93-b491-7f425f8eaef2).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 53, 33, 893000,
                                                tzinfo=tzlocal()),
                 'id': 'ad29f482-ba09-45ff-a0a6-40a4f09c4bda',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 52, 41, 173000,
                                                tzinfo=tzlocal()),
                 'id': '67d81659-6270-434c-a02d-663ac7825a84',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '394dfbf3-9bee-4361-b30a-2fa979d76518).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 36, 54, 630000,
                                                tzinfo=tzlocal()),
                 'id': '386ab757-054c-4c16-b38d-5c3b7cba20ff',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 35, 56, 681000,
                                                tzinfo=tzlocal()),
                 'id': '2e8f2752-8156-469a-aaba-c3794554d92b',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '574b0ff1-2593-4a82-ad48-f4ddd05a3d36).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 20, 13, 103000,
                                                tzinfo=tzlocal()),
                 'id': '11d4a24b-cbfd-4ab1-9696-c3c5e79f15f7',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 19, 16, 56000,
                                                tzinfo=tzlocal()),
                 'id': '0b40b2f6-a256-46ec-8ef5-ceb6bcaa38c9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'bb60b8df-6c6d-46e6-bd3b-2ac4bffc4e92).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 4, 48, 512000,
                                                tzinfo=tzlocal()),
                 'id': 'e28c7b11-f0c1-4ad4-9b27-20ef9da73031',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 4, 3, 47, 912000,
                                                tzinfo=tzlocal()),
                 'id': '802d451d-bb74-4f18-9505-f5f3dea6ecd9',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '59235234-06b1-4c8e-b992-395e6c703dca).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 49, 4, 585000,
                                                tzinfo=tzlocal()),
                 'id': 'f2bac145-51b0-44f6-84f4-95542fc8f540',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 48, 9, 346000,
                                                tzinfo=tzlocal()),
                 'id': '97c50e63-d1f3-4143-ba54-92ae94ad8673',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'ca5832dc-bffb-4f2b-92b5-4158a64ca11b).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 33, 26, 137000,
                                                tzinfo=tzlocal()),
                 'id': 'ccddc586-f40a-4f6a-80ab-73a78fbd31b9',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 32, 27, 571000,
                                                tzinfo=tzlocal()),
                 'id': 'ee7016ea-7580-4a39-928a-eda1ef31fcd1',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '46151cc3-3acc-49d8-882b-034d66579933).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 17, 8, 367000,
                                                tzinfo=tzlocal()),
                 'id': '2c5e6030-4a1a-47f9-8f52-ec36b4c09e05',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 16, 9, 859000,
                                                tzinfo=tzlocal()),
                 'id': '1d75fcc7-2e00-4453-8da4-d0a9b1ab938f',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '6af1376f-cf74-479f-ac86-7f8ea7717e77).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 1, 8, 156000,
                                                tzinfo=tzlocal()),
                 'id': 'f3df9de3-8bbb-498c-b4a5-fc54ae9b8d95',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 3, 0, 10, 519000,
                                                tzinfo=tzlocal()),
                 'id': '51ad0db5-33c9-4c43-9104-5304cf14bc79',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '8f0e9af1-7952-405e-8194-21065b509ca6).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 45, 26, 935000,
                                                tzinfo=tzlocal()),
                 'id': '341ac3bf-03ce-4f42-8607-fb11596215e3',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 44, 29, 750000,
                                                tzinfo=tzlocal()),
                 'id': '67a68854-ba81-43e2-b269-b05aaf150877',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            '561aae47-2f2a-4351-bd23-db4329a63430).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 29, 4, 234000,
                                                tzinfo=tzlocal()),
                 'id': '075b5676-44fc-4259-bb73-c82746fdd1ca',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 28, 4, 565000,
                                                tzinfo=tzlocal()),
                 'id': 'c252ad94-7bcc-4bf8-8825-1c9a908ed8a3',
                 'message': '(service purchases-web) has started 1 '
                            'tasks: (task '
                            'b4bd9f25-4c91-4f99-87e6-6354d5cb6a52).'},
                {'createdAt': datetime.datetime(2019, 2, 27, 2, 13, 35, 375000,
                                                tzinfo=tzlocal()),
                 'id': '5c5d939e-e462-4728-abf8-182585c8c7b4',
                 'message': '(service purchases-web) is unable to '
                            'consistently start tasks successfully. '
                            'For more information, see the '
                            'Troubleshooting section of the Amazon '
                            'ECS Developer Guide.'},
                {
                    'createdAt': datetime.datetime(2019, 2, 27, 2, 12, 37, 858000,
                                                   tzinfo=tzlocal()),
                    'id': 'a3e37cd5-3a1f-4d59-b99a-744a456ea347',
                    'message': '(service purchases-web) has started 1 '
                               'tasks: (task '
                               'a55604ef-5b32-4e97-8e4f-972142fef058).'
                }
            ],
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
