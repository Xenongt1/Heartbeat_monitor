# Setup Guide

## Requirements
- Docker & Docker Compose
- Python 3.9+

## Instructions
1. Start services: `docker-compose up -d`
2. Install dependencies: `pip install -r requirements.txt`
3. Run pipeline: `python pipeline/pipeline_runner.py`
4. View dashboard: `streamlit run dashboard/app.py`
