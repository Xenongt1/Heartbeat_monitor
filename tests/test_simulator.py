import unittest
from data_generator.simulator import generate_heartbeat

class TestSimulator(unittest.TestCase):
    def test_generate_heartbeat(self):
        data = generate_heartbeat()
        self.assertIn('customer_id', data)
        self.assertIn('heart_rate', data)
        self.assertIn('timestamp', data)
        self.assertIn('status', data)
        self.assertIsInstance(data['heart_rate'], int)
        self.assertTrue(30 <= data['heart_rate'] <= 150)

if __name__ == '__main__':
    unittest.main()
