# Kafka consumer
import json
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from kafka import KafkaConsumer
from consumer.validator import validate_heartbeat
from database.db_handler import insert_heartbeat
from config.kafka_config import KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME

def start_consumer():
    """Listens to Kafka topic, validates data and stores in DB."""
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='heartbeat_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        
        print(f"Consumer started. Listening on {TOPIC_NAME}...", flush=True)
        
        for message in consumer:
            data = message.value
            
            # Validate heart rate
            data['status'] = validate_heartbeat(data['heart_rate'])
            
            # Store in database
            insert_heartbeat(data)
            
            print(f"Processed: {data['customer_id']} | Rate: {data['heart_rate']} | Status: {data['status']}", flush=True)
            
    except Exception as e:
        print(f"Error in consumer: {e}", flush=True)
        print("Make sure Kafka and PostgreSQL are running.", flush=True)

if __name__ == "__main__":
    start_consumer()
