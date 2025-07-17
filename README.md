# MLOps Engineer Task – Model Serving + Deployment Pipeline

## Project Objective

Design and implement an end-to-end MLOps pipeline for serving an open-source sentiment analysis model with version-controlled deployment and monitoring.

---

## Scope of Work

- Serve an open-source sentiment analysis model (`distilbert-base-uncased-finetuned-sst-2-english`)  
- Expose model as a REST API using Flask  
- Containerize the application with Docker  
- Setup CI/CD pipeline using GitHub Actions to automate building, testing, and deployment  
- Integrate logging and inference metrics with Prometheus and Grafana  

---

## Tech Stack

- **API Framework:** Flask  
- **Model:** Hugging Face Transformers (DistilBERT)  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **Monitoring:** Prometheus + Grafana  

---

## Repository Contents

- `app.py` — Flask application with `/predict`, `/metrics`, and health endpoints  
- `Model.py` — Loads and runs the sentiment analysis pipeline  
- `Dockerfile` — Docker image configuration for the app  
- `.github/workflows/ci-cd.yml` — GitHub Actions workflow for CI/CD  
- `requirements.txt` — Python dependencies  
- `README.md` — This file  

---

