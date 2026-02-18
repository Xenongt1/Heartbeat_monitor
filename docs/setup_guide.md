# 🛠️ Detailed Setup & Deployment Guide

Follow these steps to get the Heartbeat Monitor system running on your local machine.

## 1. Prerequisites

Before starting, ensure you have the following installed:
- **Python 3.10 or higher**
- **Docker Desktop** (Make sure it is running)
- **Git**

## 2. Environment Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Xenongt1/Heartbeat_monitor.git
   cd Heartbeat_monitor
   ```

2. **Create a Virtual Environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

## 3. Infrastructure (Docker)

This project requires Kafka, Zookeeper, and PostgreSQL.

1. **Navigate to the docker folder**:
   ```powershell
   cd docker
   ```

2. **Start the services**:
   ```powershell
   docker-compose up -d
   ```
   > [!NOTE]
   > We are using port **5433** for PostgreSQL to avoid conflicts with existing local Postgres installations.

3. **Verify services are running**:
   ```powershell
   docker ps
   ```
   You should see `docker-kafka-1`, `docker-postgres-1`, and `docker-zookeeper-1` in the list.

## 4. Configuration (.env)

The project uses environment variables. Ensure you have a `.env` file in the **root** of the project:

```text
# Kafka settings
KAFKA_BOOTSTRAP_SERVERS=127.0.0.1:9092
KAFKA_TOPIC_NAME=heartbeat_data

# Database settings
DB_HOST=localhost
DB_PORT=5433
DB_NAME=heartbeat_db
DB_USER=admin
DB_PASSWORD=password
```

## 5. Running the Application

1. **Start the Data Pipeline**:
   From the project **root**, run the orchestrator. This starts both the data generator (Producer) and the processor (Consumer).
   ```powershell
   python pipeline/pipeline_runner.py
   ```
   You should see logs indicating data is being sent and processed.

2. **Launch the Dashboard**:
   Open a **new terminal**, activate the venv, and run:
   ```powershell
   streamlit run dashboard/app.py
   ```
   Your browser will automatically open to `http://localhost:8501`.

## 🛠️ Troubleshooting

### Kafka connection error (NoBrokersAvailable)
- Ensure Docker is running and all containers are "Started".
- If on Windows, try using `127.0.0.1` instead of `localhost` in your `.env`.

### Database Authentication Failed
- If you change credentials in `.env`, you must reset the DB container:
  ```powershell
  cd docker
  docker-compose down -v
  docker-compose up -d
  ```

### Port 5432/5433 already in use
- This project uses **5433**. If that is also taken, update the `ports` mapping in `docker/docker-compose.yml` and the `DB_PORT` in `.env`.
