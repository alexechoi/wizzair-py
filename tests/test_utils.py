import unittest
from datetime import datetime
from wizzair.utils import parse_date

class TestUtils(unittest.TestCase):
    def test_parse_date(self):
        date_str = "2024-12-01T16:50:00"
        parsed_date = parse_date(date_str)
        self.assertIsInstance(parsed_date, datetime)
        self.assertEqual(parsed_date.year, 2024)
        self.assertEqual(parsed_date.month, 12)
        self.assertEqual(parsed_date.day, 1)

if __name__ == "__main__":
    unittest.main()