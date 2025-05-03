def create_task_definition(execution_role, memory, cpu, deployment_type, task_role='', ):
    task_definition = {
        "networkMode": "awsvpc" if deployment_type != 'EXTERNAL' else 'bridge',
        "taskRoleArn": task_role,
        "containerDefinitions": [],
        "executionRoleArn": execution_role,
        "requiresCompatibilities": [
            deployment_type
        ],
        "memory": str(memory),
        "cpu": str(cpu)
    }

    return task_definition


def create_container_definition(env_vars, environment, project_name, container_name, ecr_path, command, cpu=256,
                                memory=512, ports=None, disable_logs=False, region_name="eu-west-1"):
    container_definition_name = f"{project_name}-{container_name}"
    log_path = f"/ecs/{environment}-{project_name}-{container_name}"

    port_mappings = []

    if ports:
        for p in ports:
            host_port = int(p.split(':')[0])
            container_port = int(p.split(':')[1])

            port_mappings.append({
                "hostPort": host_port,
                "protocol": "tcp",
                "containerPort": container_port
            })

    container_definition = {
        "environment": env_vars,
        "name": container_definition_name,
        "mountPoints": [],
        "image": ecr_path,
        "cpu": cpu,
        "memory": memory,
        "portMappings": port_mappings,
        "command": parse_command(command),
        "essential": True,
        "volumesFrom": []
    }

    if not disable_logs:
        container_definition["logConfiguration"] = {
            "logDriver": "awslogs",
            "options": {
                "awslogs-stream-prefix": "ecs",
                "awslogs-group": log_path,
                "awslogs-region": region_name
            }
        }

    return container_definition


def parse_command(cmd):
    return cmd.split(' ')
