from ecs_deployer.vault import VaultManager


def build_secrets_manager(secrets_manager_config):
    if all(value for value in secrets_manager_config.values()) and secrets_manager_config.get('name') == 'vault':
        return VaultManager(secrets_manager_config)
    return None
