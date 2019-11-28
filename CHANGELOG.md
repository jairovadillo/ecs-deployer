# CHANGELOG

## 0.1.0 (18-11-2019)

### Changes:
 - Add task role to avoid use access keys 
   - Breaking changes: Task role for ECS is required with standard ARN structure. If microservice does not require task role, TASK_ROLE environment variable must be exported with empty value(export TASK_ROLE="") before launch ecs_deployer

## 0.0.7 (12-07-2019) 

#### Changes:
 - Add waiter on getLogsEvents in case of migrations failure.
 
## 0.0.6 (5-07-2019) 

#### Changes:
- Adapt vault path to kv2
 
