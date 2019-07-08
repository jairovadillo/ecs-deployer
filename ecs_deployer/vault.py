import hvac


def get_configuration_vars(host: str, token: str, path: str) -> list:
    client = hvac.Client(url=host, token=token)
    response = client.read(path)
    resp_data = response.get('data')

    # Compatible KV V1 and KV V2
    if resp_data and 'data' in resp_data and 'metadata' in resp_data:
        env_vars = resp_data.get('data')
    else:
        env_vars = resp_data


    return [{"name": k, "value": v} for k, v in env_vars.items()]
