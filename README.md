# ECS Deployer

![doge](./doge.webp)

## What it does?

- Grab environmental variables from Vault
- Register new Task Definitions based on `procfile.yml`
- Run a release phase
- Update all services with the new task definitions
- Waits until all tasks/"perros" have the new task definition

## How to run it?

- (Recommended) Create a `docker.env` file with all the environment variables needed:
    - _VAULT_HOST_
    - _VAULT_TOKEN_
    - _VAULT_PATH_
    - _ENVIRONMENT_
    - _PROJECT_NAME_
    - _ECR_PATH_
    - _PROCFILE_LOCATION_
    - _ACCOUNT_ID_
    - _ROLE_NAME_
    - _EXECUTION_ROLE_
- Create a `procfile.yml` following this format:

    ```yaml
    service1:
      command: python run_server.py
      memory: 512
      cpu: 256
    service2:
      command: python run_worker.py
      memory: 1024
      cpu: 512
    release:
      command: python migrations.py
      memory: 512
      cpu: 256
    ```

- On your project root run:

    ```bash
    docker run --env-file=docker.env -v $(pwd)/procfile.yml:/app/procfile.yml -it ecs_deployer
    ```
- Enjoy!
