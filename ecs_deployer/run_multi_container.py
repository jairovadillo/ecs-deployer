import argparse
import logging

import conf
from services import register_task_definitions_multi_container, wait_for_release_task, check_deployment, \
    update_services, run_release_cmd_multi_container

parser = argparse.ArgumentParser(description='Parse params for deployment')
parser.add_argument("-i", "--image", type=str, required=True)
parser.add_argument("-c", "--container", type=str, required=True)

logging.getLogger().setLevel(logging.INFO)


def main(ecr_image: str, container_definitions: str) -> None:
    logging.info("Registering task definitions")

    revisions = register_task_definitions_multi_container(container_definitions,
                                                          {
                                                              'host': conf.VAULT_HOST,
                                                              'token': conf.VAULT_TOKEN,
                                                              'path': conf.VAULT_PATH
                                                          },
                                                          conf.EXECUTION_ROLE,
                                                          conf.ENVIRONMENT,
                                                          conf.PROJECT_NAME,
                                                          ecr_image)

    revisions.pop('release', None)

    logging.info("Running release command")
    task_tracker = run_release_cmd_multi_container(container_definitions,
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
        main(ecr_image=args.image, container_definitions=args.container)
    except Exception as e:
        logging.critical(str(e))
        raise Exception(e)
