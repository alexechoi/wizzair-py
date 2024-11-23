import unittest
from wizzair.api import Wizzair

class TestWizzairAPI(unittest.TestCase):
    def setUp(self):
        self.api = Wizzair(currency="GBP")
        self.departure_station = "LGW"
        self.months = 6

    def test_get_cheapest_flights(self):
        print("\nRunning test_get_cheapest_flights...")
        flights = self.api.get_cheapest_flights(self.departure_station, self.months, discounted_only=False)
        self.assertIsInstance(flights, list)
        print(f"Fetched {len(flights)} flights.")
        if flights:
            first_flight = flights[0]
            print("Sample flight details:", first_flight)
            self.assertIn("departureStation", first_flight)
            self.assertIn("arrivalStation", first_flight)
            self.assertIn("std", first_flight)

if __name__ == "__main__":
    unittest.main()