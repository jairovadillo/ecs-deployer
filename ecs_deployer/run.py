import argparse
import logging

import conf

from factories import build_secrets_manager
from services import register_task_definitions, run_release_cmd, wait_for_release_task, check_deployment, \
    update_services

parser = argparse.ArgumentParser(description='Parse params for deployment')
parser.add_argument("-p", "--procfile", type=str, required=True)
parser.add_argument("-i", "--image", type=str, required=True)
parser.add_argument("-d", "--driver", type=str, required=True)

logging.getLogger().setLevel(logging.INFO)

drivers_config = {
    'vault': {
        'host': conf.VAULT_HOST,
        'token': conf.VAULT_TOKEN,
        'path': conf.VAULT_PATH
    },
    'aws_secrets_manager': {}
}


def main(procfile_path: str, ecr_image: str, driver: str) -> None:
    logging.info("Registering task definitions")
    secrets_manager = build_secrets_manager(driver=driver,
                                            secrets_manager_config=drivers_config.get(driver)) if driver else None
    revisions = register_task_definitions(procfile_path,
                                          conf.EXECUTION_ROLE,
                                          conf.ENVIRONMENT,
                                          conf.PROJECT_NAME,
                                          conf.TASK_ROLE,
                                          ecr_image,
                                          secrets_manager=secrets_manager
                                          )

    revisions.pop('release', None)

    logging.info("Running release command")
    task_tracker = run_release_cmd(procfile_path,
                                   conf.CLUSTER_NAME,
                                   conf.ENVIRONMENT,
                                   conf.PROJECT_NAME)

    if task_tracker:
        try:
            logging.info("Waiting for release task to finish ({})".format(task_tracker))
            wait_for_release_task(conf.CLUSTER_NAME, task_tracker)
        except Exception as e:
            logging.error("Error executing migrations: {}".format(e))
            raise e

    logging.info("Updating services")
    update_services(conf.CLUSTER_NAME, conf.ENVIRONMENT, conf.PROJECT_NAME, revisions)

    logging.info("Checking deployment")
    check_deployment('{}-21b'.format(conf.ENVIRONMENT), conf.PROJECT_NAME, revisions)


if __name__ == "__main__":
    args, unknown = parser.parse_known_args()

    try:
        main(procfile_path=args.procfile, ecr_image=args.image)
    except Exception as e:
        logging.critical(str(e))
        raise Exception(e)
