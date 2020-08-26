from typing import List

import hvac


class VaultManager:

    def __init__(self, vault_manager_config):
        self.host = vault_manager_config['host']
        self.token = vault_manager_config['token']
        self.path = vault_manager_config['path']

    def build(self, vault_manager_config):
        if all(value for value in vault_manager_config.values()):
            return self.__init__(vault_manager_config)

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
