from kafka import KafkaProducer
import json

print("Connecting to Kafka...")
try:
    producer = KafkaProducer(
        bootstrap_servers=['127.0.0.1:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        request_timeout_ms=5000
    )
    print("Connected!")
    producer.send('test-topic', {'test': 'message'})
    print("Sent!")
    producer.flush()
    print("Flushed!")
except Exception as e:
    print(f"Failed: {e}")
