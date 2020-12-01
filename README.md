# ECS Deployer

![doge](./doge.webp)

## What it does?

- Grab environmental variables from Vault
- Register new Task Definitions based on `procfile.yml`
- Run a release phase (migrations or whatever)
- Update all ECS services with the new task definitions
- Waits until all tasks/"perros" have the new task definition

## Builds & CI

DockerHub automatically tests and builds the image tags: [DockerHub Repo](https://cloud.docker.com/u/21buttons/repository/docker/21buttons/ecs-deployer/general)

## Preconditions:

- FARGATE Cluster is already created
- Services are defined by _PROJECT_NAME-SERVICE-NAME_
- The provided AWS credentials are used to assume another role only
- AWS families are defined as _ENV-PROJECT_NAME-SERVICE_NAME_
- There's a _web_ service
- Deploys will finish in less than 15 minutes
- The docker image you want to deploy is already on ECR (or publicly available on other registry)

## Running tests

`docker-compose -f docker-compose.test.yml up`

## How to run it?

- (Recommended) Create a `docker.env` file with all the environment variables needed:
    - _ENVIRONMENT_
    - _PROJECT_NAME_
    - _AWS_ACCESS_KEY_ID_
    - _AWS_SECRET_ACCESS_KEY_
    - _AWS_DEFAULT_REGION_
    - _ACCOUNT_ID_
    - _ROLE_NAME_
    - _EXECUTION_ROLE_
    - _CLUSTER_NAME_
    - (*) _VAULT_HOST_
    - (*) _VAULT_TOKEN_
    - (*) _VAULT_PATH_
    - (*) _AWS_SECRET_NAME_ 
    
    * optional
    
- Create a `procfile.yml` following this format:

    ```yaml
    service1:
      command: python run_server.py
      memory: 512
      cpu: 256
      ports:
        - 8000:8000
        - 2222:2222
      disable-logs: true
    service2:
      command: python run_worker.py
      memory: 1024
      cpu: 512
    release:
      command: python migrations.py
      memory: 512
      cpu: 256
    ```
- Deployer parameters are:
    - `-p` The procfile path
    - `-i` ECR image path (also works with any public image)
    - `-d` (Optional) The desired secret manager service (aws_secrets_manager or vault)
    
- Example run:

    ```bash
    docker run --rm --env-file=local.env -v $(pwd):/code -it ecs_deployer deploy -p /code/procfile.yml -i << ecr_path>> -d aws_secrets_manager
    ```
    
- Enjoy!
