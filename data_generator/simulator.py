# Heartbeat data simulator
import random
import time
from datetime import datetime
import uuid

def generate_heartbeat(customer_id=None):
    """Generates fake customer heartbeat data."""
    if not customer_id:
        customer_id = f"CUST_{random.randint(100, 999)}"
    
    # Simulate a realistic heart rate with occasional anomalies
    # Normal: 60-100, Bradycardia: <60, Tachycardia: >100
    base_rate = 75
    variation = random.randint(-15, 15)
    
    # 5% chance of an anomaly
    if random.random() < 0.05:
        heart_rate = random.choice([random.randint(40, 55), random.randint(110, 160)])
    else:
        heart_rate = base_rate + variation

    return {
        "customer_id": customer_id,
        "heart_rate": heart_rate,
        "timestamp": datetime.now().isoformat(),
        "status": "pending" # To be updated by validator
    }

if __name__ == "__main__":
    # Test the simulator
    for _ in range(5):
        print(generate_heartbeat())
        time.sleep(1)
