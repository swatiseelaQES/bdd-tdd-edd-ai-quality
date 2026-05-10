import os
import urllib3
import requests

BASE_URL = os.getenv("BOOKING_API_BASE_URL", "https://restful-booker.herokuapp.com")

VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() == "true"

if not VERIFY_SSL:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def valid_booking_payload() -> dict:
    return {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-01-01",
            "checkout": "2026-01-05"
        },
        "additionalneeds": "Breakfast"
    }


def create_booking(payload: dict) -> requests.Response:
    return requests.post(
        f"{BASE_URL}/booking",
        json=payload,
        timeout=15,
        verify=VERIFY_SSL
    )
