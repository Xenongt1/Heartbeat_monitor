import unittest
from consumer.validator import validate_heartbeat

class TestValidator(unittest.TestCase):
    def test_validate_normal(self):
        self.assertEqual(validate_heartbeat(75), 'NORMAL')
        self.assertEqual(validate_heartbeat(100), 'NORMAL')
        self.assertEqual(validate_heartbeat(60), 'NORMAL')

    def test_validate_tachycardia(self):
        self.assertEqual(validate_heartbeat(111), 'TACHYCARDIA')
        self.assertEqual(validate_heartbeat(150), 'TACHYCARDIA')

    def test_validate_bradycardia(self):
        self.assertEqual(validate_heartbeat(49), 'BRADYCARDIA')
        self.assertEqual(validate_heartbeat(40), 'BRADYCARDIA')

if __name__ == '__main__':
    unittest.main()
