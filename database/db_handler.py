# Database handler
import psycopg2
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.db_config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
from config.logger_config import setup_logger
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

logger = setup_logger("DatabaseHandler", "logs/heartbeat.log")

@retry(
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=10),
    retry=retry_if_exception_type(psycopg2.OperationalError),
    before_sleep=lambda retry_state: logger.warning(f"Retrying database connection (attempt {retry_state.attempt_number})...")
)
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        connect_timeout=5
    )

def init_db():
    """Initialize the database using schema.sql."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        schema_path = os.path.join(os.path.dirname(__file__), 'schema.sql')
        with open(schema_path, 'r') as f:
            cur.execute(f.read())
            
        conn.commit()
        cur.close()
        logger.info("Database initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")
    finally:
        if conn is not None:
            conn.close()

def insert_heartbeat(data):
    """Insert heartbeat data into PostgreSQL."""
    conn = None
    try:
        conn = get_connection()
        cur = conn.cursor()
        
        insert_query = """
        INSERT INTO heartbeat_logs (customer_id, heart_rate, status, timestamp)
        VALUES (%s, %s, %s, %s)
        """
        
        cur.execute(insert_query, (
            data['customer_id'],
            data['heart_rate'],
            data['status'],
            data['timestamp']
        ))
        
        conn.commit()
        cur.close()
        # logger.debug(f"Inserted to DB: {data['customer_id']}")
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(f"Database error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    # Test connection
    try:
        conn = get_connection()
        logger.info("Database connection successful!")
        conn.close()
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
