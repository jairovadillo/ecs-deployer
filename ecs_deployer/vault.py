import hvac


def get_configuration_vars(host: str, token: str, path: str) -> list:
    client = hvac.Client(url=host, token=token)
    response = client.read(path)
    data = response.get('data')

    # Compatible KV V1 and KV V2
    if data and len(data) == 2 and 'data' in data and 'metadata' in data:
        env_vars = data.get('data')
    else:
        env_vars = data


    return [{"name": k, "value": v} for k, v in env_vars.items()]
