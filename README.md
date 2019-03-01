# ECS Deployer

![doge](./doge.webp)

## What it does?

- Grab environmental variables from Vault
- Register new Task Definitions based on `procfile.yml`
- Run a release phase
- Update all services with the new task definitions
- Waits until all tasks/"perros" have the new task definition

## Preconditions:

- Cluster is already created
- Services are defined by _PROJECT_NAME-SERVICE-NAME_
- The provided AWS credentials are used to assume another role only
- AWS families are defined as _ENV-PROJECT_NAME-SERVICE_NAME_
- There's a _web_ service
- Vault is used (Optional in the future -> AWS KMS)
- Deploys will finish in less than 15 minutes
- FARGATE is being used
- The image you want to deploy is already on ECR

## How to run it?

- (Recommended) Create a `docker.env` file with all the environment variables needed:
    - _VAULT_HOST_
    - _VAULT_TOKEN_
    - _VAULT_PATH_
    - _ENVIRONMENT_
    - _PROJECT_NAME_
    - _ECR_PATH_
    - _AWS_ACCESS_KEY_ID_
    - _AWS_SECRET_ACCESS_KEY_
    - _AWS_DEFAULT_REGION_
    - _ACCOUNT_ID_
    - _ROLE_NAME_
    - _EXECUTION_ROLE_
    - _CLUSTER_NAME_
    - _PROCFILE_NAME_
    
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
