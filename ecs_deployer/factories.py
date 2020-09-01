from typing import Any, Dict
from secret_managers import AWSSecretManager, VaultManager


def build_secrets_manager(driver: str, secrets_manager_config: Dict[str, Any]):
    if driver == 'vault':
        return VaultManager.build(secrets_manager_config)
    if driver == 'aws':
        return AWSSecretManager.build(secrets_manager_config)

    raise NotImplementedError('Driver not implemented: {}'.format(driver))
