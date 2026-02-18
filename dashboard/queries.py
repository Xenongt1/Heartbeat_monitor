# Dashboard queries
import pandas as pd
import sys
import os

# Add project root to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.db_handler import get_connection

def get_recent_logs(limit=100):
    """Fetch recent heartbeat logs from the database."""
    try:
        conn = get_connection()
        query = f"SELECT customer_id, heart_rate, status, timestamp FROM heartbeat_logs ORDER BY timestamp DESC LIMIT {limit}"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return pd.DataFrame()

def get_stats():
    """Fetch summary statistics."""
    try:
        conn = get_connection()
        query = "SELECT status, COUNT(*) as count FROM heartbeat_logs GROUP BY status"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    except Exception as e:
        print(f"Error fetching stats: {e}")
        return pd.DataFrame()
