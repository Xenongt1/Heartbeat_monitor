from kafka import KafkaConsumer
import json

print("Connecting to Kafka Consumer...")
try:
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers=['127.0.0.1:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        consumer_timeout_ms=5000
    )
    print("Connected!")
    for message in consumer:
        print(f"Received: {message.value}")
except Exception as e:
    print(f"Failed: {e}")
