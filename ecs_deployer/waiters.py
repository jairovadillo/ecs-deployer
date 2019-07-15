from botocore.waiter import WaiterModel, create_waiter_with_client


class GetEventLogWaiter:

    @classmethod
    def wait(cls, log_group_name, log_stream_name, aws_client):

        waiter_name = "GetLogEventsWaiter"

        waiter_config = {
            'version': 2,
            'waiters': {
                'GetLogEventsWaiter': {
                    'delay': 10,
                    "maxAttempts": 10,
                    'operation': 'GetLogEvents',
                    "acceptors": [
                        {
                            "expected": "ResourceNotFoundException",
                            "matcher": "error",
                            "state": "retry"
                        },
                        {
                            "matcher": "status",
                            "expected": 200,
                            "state": "success"
                        }
                    ]
                }
            }
        }
        waiter_model = WaiterModel(waiter_config)
        waiter = create_waiter_with_client(waiter_name, waiter_model, aws_client)
        waiter.wait(logGroupName=log_group_name,
                    logStreamName=log_stream_name
                    )
