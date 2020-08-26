from ecs_deployer.vault import VaultManager


def build_secrets_manager(driver, secrets_manager_config):
    if driver == 'vault':
        return VaultManager.build(secrets_manager_config)
    return None
