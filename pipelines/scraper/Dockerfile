FROM python:3.9.15-slim
WORKDIR /app
COPY ./pipelines/scraper/requirements.txt .
RUN pip install -r requirements.txt
COPY ./pipelines/scraper /app/pipelines/scraper
COPY ./storages /app/storages/
COPY ./utils /app/utils/
ENTRYPOINT [ "python3", "/app/pipelines/scraper/main.py"]
