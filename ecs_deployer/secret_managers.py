import base64
import json
import logging
from abc import ABC, abstractmethod
from typing import Any, Dict, List

import boto3
import hvac
from botocore.exceptions import ClientError


class SecretsManager(ABC):
    @abstractmethod
    def get_configuration_vars(self) -> List[Dict[str, str]]:
        pass


class VaultManager(SecretsManager):

    def __init__(self, host: str, token: str, path: str):
        self.host = host
        self.token = token
        self.path = path

    @classmethod
    def build(cls, vault_manager_config: Dict[str, Any]) -> 'VaultManager':
        try:
            return cls(vault_manager_config['host'], vault_manager_config['token'], vault_manager_config['path'])
        except KeyError as e:
            logging.error("Missing key for vault manager: {}".format(e))
            raise e

    def get_configuration_vars(self) -> List[Dict[str, str]]:
        client = hvac.Client(url=self.host, token=self.token)
        response = client.read(self.path)
        data = response.get('data')

        # Compatible KV V1 and KV V2
        if data and len(data) == 2 and 'data' in data and 'metadata' in data:
            env_vars = data.get('data')
        else:
            env_vars = data

        return [{"name": k, "value": v} for k, v in env_vars.items()]


class AWSSecretManager(SecretsManager):
    def __init__(self, secret_name: str, region_name: str):
        self.secret_name = secret_name
        self.region_name = region_name

    @classmethod
    def build(cls, manager_config: Dict[str, Any]) -> 'AWSSecretManager':
        try:
            return cls(manager_config['secret_name'], manager_config['region_name'])
        except KeyError as e:
            logging.error("Missing key for aws secret manager: {}".format(e))
            raise e

    def get_configuration_vars(self) -> List[Dict[str, str]]:
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )

        try:
            get_secret_value_response = client.get_secret_value(
                SecretId=self.secret_name
            )
        except ClientError as e:
            if e.response['Error']['Code'] == 'DecryptionFailureException':
                # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InternalServiceErrorException':
                # An error occurred on the server side.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidParameterException':
                # You provided an invalid value for a parameter.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'InvalidRequestException':
                # You provided a parameter value that is not valid for the current state of the resource.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            elif e.response['Error']['Code'] == 'ResourceNotFoundException':
                # We can't find the resource that you asked for.
                # Deal with the exception here, and/or rethrow at your discretion.
                raise e
            else:
                raise e
        else:
            secrets: Dict[str, str] = dict()
            # Decrypts secret using the associated KMS CMK.
            # Depending on whether the secret is a string or binary, one of these fields will be populated.
            if 'SecretString' in get_secret_value_response:
                secret = get_secret_value_response['SecretString']
                secrets = json.loads(secret)
            else:
                decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
                secrets = json.loads(decoded_binary_secret)

            return [{"name": k, "value": v} for k, v in secrets.items()]
