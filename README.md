# Heartbeat Monitor Project

## Overview
This project monitors customer heartbeat data in real-time using Kafka, PostgreSQL, and Python.

## Structure
- `docker/`: Infrastructure services (Kafka, Zookeeper, PostgreSQL)
- `config/`: Configuration settings
- `data_generator/`: Simulator for heartbeat data
- `producer/`: Service to send data to Kafka
- `consumer/`: Service to process and validate data
- `database/`: DB schema and handlers
- `pipeline/`: Orchestration logic
- `dashboard/`: Visualization (Streamlit/Dash)
- `tests/`: Unit and integration tests
- `docs/`: Documentation and diagrams
- `logs/`: Runtime logs
