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
from tenacity import retry, wait_fixed, stop_after_attempt

@retry(
    stop=stop_after_attempt(10),
    wait=wait_fixed(5),
    before_sleep=lambda retry_state: print(f"Kafka Producer: Retrying connection to broker (attempt {retry_state.attempt_number})...", flush=True)
)
def get_producer():
    return KafkaProducer(
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',
        retries=5, # Kafka internal retries
        retry_backoff_ms=1000,
        request_timeout_ms=10000
    )

def start_producer(interval=1.0):
    """Reads from simulator, sends to Kafka topic."""
    try:
        producer = get_producer()
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
