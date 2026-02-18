import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Kafka configuration
KAFKA_BOOTSTRAP_SERVERS = os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092').split(',')
TOPIC_NAME = os.getenv('KAFKA_TOPIC_NAME', 'heartbeat_data')
