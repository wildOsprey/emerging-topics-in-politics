FROM python:3.9.15-slim
WORKDIR /app
COPY ./pipelines/sentiment/requirements.txt .
RUN pip install -r requirements.txt


COPY ./pipelines/sentiment /app/pipelines/sentiment
COPY ./algorithms /app/algorithms/
COPY ./storages /app/storages/
COPY ./utils /app/utils/

ENTRYPOINT [ "python3", "/app/pipelines/sentiment/main.py"]
CMD ["--elastic-hosts", "https://elastic:OLVzrQ1YsIU91dIL@localhost:9200", "--index", "test_run"]
