FROM python:3.9.15-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python3", "main.py"]
CMD ["--host", "127.0.0.1","--port", "8000", "--tags", "ua,war", "--count", "1", "--times", "2"]