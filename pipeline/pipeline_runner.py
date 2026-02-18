# Pipeline runner
import multiprocessing
import time
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from producer.kafka_producer import start_producer
from consumer.kafka_consumer import start_consumer
from database.db_handler import init_db

def run_pipeline():
    """Orchestrates producer + consumer together using multiprocessing."""
    
    # Initialize DB
    init_db()
    
    # Create processes
    producer_process = multiprocessing.Process(target=start_producer, args=(2.0,)) # Send every 2 seconds
    consumer_process = multiprocessing.Process(target=start_consumer)
    
    print("Starting Pipeline... (Ctrl+C to stop)", flush=True)
    
    try:
        # Start processes
        producer_process.start()
        # Give producer a moment to start
        time.sleep(2)
        consumer_process.start()
        
        # Keep main thread alive
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nShutting down pipeline...", flush=True)
        producer_process.terminate()
        consumer_process.terminate()
        print("Pipeline stopped.", flush=True)

if __name__ == "__main__":
    run_pipeline()
