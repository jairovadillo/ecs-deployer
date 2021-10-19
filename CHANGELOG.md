# CHANGELOG

## 0.1.2 (2021-10-19)

### Changes:
 - Add deployment-type (EXTERNAL/FARGATE) parameter to procfile.yml

## 0.1.1 (2020-04-20)

### Changes:
 - Add disable-logs parameter to procfile.yml

## 0.1.0 (2019-11-18)

### Changes:
 - Add task role to avoid use access keys 
   - Breaking changes: Task role for ECS is required with standard ARN structure. If microservice does not require task role, TASK_ROLE environment variable must be exported with empty value(export TASK_ROLE="") before launch ecs_deployer

## 0.0.7 (2019-07-12) 

#### Changes:
 - Add waiter on getLogsEvents in case of migrations failure.
 
## 0.0.6 (2019-07-05) 

#### Changes:
- Adapt vault path to kv2
 
