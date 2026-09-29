FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app.py .
COPY tuned_logistic_pipeline.pkl .

# Add healthcheck
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

RUN ls -la tuned_logistic_pipeline.pkl

EXPOSE 8501

# Modified command to ensure proper network binding
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--browser.serverAddress=localhost"]