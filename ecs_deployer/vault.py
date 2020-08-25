import hvac


class VaultManager:

    def __init__(self, secrets_manager_config):
        self.host = secrets_manager_config.get('host')
        self.token = secrets_manager_config('token')
        self.path = secrets_manager_config('path')

    def get_configuration_vars(self) -> list:
        client = hvac.Client(url=self.host, token=self.token)
        response = client.read(self.path)
        data = response.get('data')

        # Compatible KV V1 and KV V2
        if data and len(data) == 2 and 'data' in data and 'metadata' in data:
            env_vars = data.get('data')
        else:
            env_vars = data

        return [{"name": k, "value": v} for k, v in env_vars.items()]
