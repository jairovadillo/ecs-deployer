import hvac


def get_configuration_vars(host: str, token: str, path: str) -> list:
    client = hvac.Client(url=host, token=token)
    response = client.read(path)
    env_vars = response.get('data', {}).get('data')

    return [{"name": k, "value": v} for k, v in env_vars.items()]
