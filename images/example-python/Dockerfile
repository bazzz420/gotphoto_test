FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ingestor.py ./
COPY models.py ./
COPY report.py ./
COPY ingestion_config.json ./
