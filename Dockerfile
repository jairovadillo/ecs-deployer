FROM python:3.6-alpine

COPY requirements.txt /

RUN pip install -r /requirements.txt

COPY ./app/* /app/

WORKDIR /app

CMD ["python", "run.py"]