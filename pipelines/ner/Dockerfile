FROM python:3.9.15-slim
WORKDIR /app
COPY ./pipelines/ner/requirements.txt .
RUN pip install -r requirements.txt

COPY ./algorithms /app/algorithms/
COPY ./storages /app/storages/
COPY ./utils /app/utils/
COPY ./pipelines/ner /app/pipelines/ner

ENTRYPOINT [ "python3", "/app/pipelines/ner/main.py"]
