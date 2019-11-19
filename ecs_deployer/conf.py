import os


VAULT_HOST = os.getenv('VAULT_HOST', None)
VAULT_TOKEN = os.getenv('VAULT_TOKEN', None)
VAULT_PATH = os.getenv('VAULT_PATH', None)

EXECUTION_ROLE = os.environ['EXECUTION_ROLE']

PROJECT_NAME = os.environ['PROJECT_NAME']

ACCOUNT_ID = os.environ['ACCOUNT_ID']
ROLE_NAME = os.environ['ROLE_NAME']

CLUSTER_NAME = os.environ['CLUSTER_NAME']

ENVIRONMENT = os.environ['ENVIRONMENT']

TASK_ROLE = os.getenv('TASK_ROLE', f'arn:aws:iam::{ACCOUNT_ID}:role/ecs/{ENVIRONMENT}-{PROJECT_NAME}-ecs-task-role')
