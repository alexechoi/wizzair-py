import requests
from datetime import datetime, timedelta
from typing import List, Dict

class Wizzair:
    def __init__(self, currency: str = "GBP"):
        self.base_url = "https://be.wizzair.com/26.0.0/Api/search/CheapFlights"
        self.currency = currency
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json, text/plain, */*",
            "Origin": "https://wizzair.com",
            "Referer": "https://wizzair.com",
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
            ),
        }

    def get_cheapest_flights(self, departure_station: str, months: int, discounted_only: bool = False) -> List[Dict]:
        payload = {
            "departureStation": departure_station,
            "months": months,
            "discountedOnly": discounted_only,
        }
        response = requests.post(self.base_url, headers=self.headers, json=payload)

        if response.status_code == 200:
            return response.json().get("items", [])
        else:
            response.raise_for_status()