# Database models
class HeartbeatLog:
    def __init__(self, customer_id, heart_rate, status, timestamp=None):
        self.customer_id = customer_id
        self.heart_rate = heart_rate
        self.status = status
        self.timestamp = timestamp
