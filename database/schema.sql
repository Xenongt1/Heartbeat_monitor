# Database schema
CREATE TABLE IF NOT EXISTS heartbeat_logs (
    id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50),
    heart_rate INT,
    status VARCHAR(20),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);