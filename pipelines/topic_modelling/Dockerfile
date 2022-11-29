FROM python:3.9.15-slim
WORKDIR /app
COPY ./pipelines/topic_modelling/requirements.txt .
RUN pip install -r requirements.txt


COPY ./pipelines/topic_modelling /app/pipelines/topic_modelling
COPY ./algorithms /app/algorithms/
COPY ./storages /app/storages/
COPY ./utils /app/utils/

ENTRYPOINT [ "python3", "/app/pipelines/topic_modelling/main.py"]
