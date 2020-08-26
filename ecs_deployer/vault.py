import logging
from typing import List

import hvac


class VaultManager:

    def __init__(self, host: str, token: str, path: str):
        self.host = host
        self.token = token
        self.path = path

    @classmethod
    def build(cls, vault_manager_config):
        try:
            return cls(vault_manager_config['host'], vault_manager_config['token'], vault_manager_config['path'])
        except KeyError as e:
            logging.error("Missing key for vault manager: {}".format(e))
            raise e

    def get_configuration_vars(self) -> List:
        client = hvac.Client(url=self.host, token=self.token)
        response = client.read(self.path)
        data = response.get('data')

        # Compatible KV V1 and KV V2
        if data and len(data) == 2 and 'data' in data and 'metadata' in data:
            env_vars = data.get('data')
        else:
            env_vars = data

        return [{"name": k, "value": v} for k, v in env_vars.items()]
