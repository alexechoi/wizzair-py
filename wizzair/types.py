from typing import NamedTuple

class Flight(NamedTuple):
    departure_time: str
    flight_number: str
    price: float
    currency: str
    origin: str
    destination: str

class Trip(NamedTuple):
    total_price: float
    outbound: Flight
    inbound: Flight