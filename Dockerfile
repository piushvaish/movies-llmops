# app/Dockerfile

FROM python:3.10-slim

WORKDIR /app
COPY /app /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8501 

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


CMD streamlit run app.py \
    --server.headless true \
    --browser.serverAddress="0.0.0.0" \
    --server.enableCORS false \
    --browser.gatherUsageStats false