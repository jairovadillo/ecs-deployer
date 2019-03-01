import os

PROCFILE_NAME = os.environ['PROCFILE_NAME']

VAULT_HOST = os.getenv('VAULT_HOST', None)
VAULT_TOKEN = os.getenv('VAULT_TOKEN', None)
VAULT_PATH = os.getenv('VAULT_PATH', None)

EXECUTION_ROLE = os.environ['EXECUTION_ROLE']

PROJECT_NAME = os.environ['PROJECT_NAME']

ECR_PATH = os.environ['ECR_PATH']

ACCOUNT_ID = os.environ['ACCOUNT_ID']
ROLE_NAME = os.environ['ROLE_NAME']

CLUSTER_NAME = os.environ['CLUSTER_NAME']

ENVIRONMENT = os.environ['ENVIRONMENT']
