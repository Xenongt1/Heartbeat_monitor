import unittest
from database.db_handler import get_connection

class TestDatabaseHandler(unittest.TestCase):
    def test_database_connection(self):
        """Test if the database is reachable."""
        try:
            conn = get_connection()
            self.assertIsNotNone(conn)
            conn.close()
        except Exception as e:
            self.fail(f"Database connection failed: {e}")

if __name__ == '__main__':
    unittest.main()
