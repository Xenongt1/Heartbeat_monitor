# Kafka producer
import json
import time
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kafka import KafkaProducer
from data_generator.simulator import generate_heartbeat
from config.kafka_config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME

def start_producer(interval=1.0):
    """Reads from simulator, sends to Kafka topic."""
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            # Wait for broker to acknowledge message
            acks='all'
        )
        print(f"Producer started. Sending data to {TOPIC_NAME} every {interval}s...", flush=True)
        
        while True:
            data = generate_heartbeat()
            producer.send(TOPIC_NAME, data)
            print(f"Sent: {data}", flush=True)
            time.sleep(interval)
            
    except Exception as e:
        print(f"Error in producer: {e}", flush=True)
        print("Make sure Kafka is running (docker-compose up -d)", flush=True)

if __name__ == "__main__":
    start_producer()
