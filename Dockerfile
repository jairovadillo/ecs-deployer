FROM python:3.6-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY ecs_deployer /app/ecs_deployer

WORKDIR /app

ENTRYPOINT ["python", "ecs_deployer/run.py"]
