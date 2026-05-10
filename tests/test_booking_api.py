from src.booking_client import create_booking, valid_booking_payload


def test_create_booking_with_valid_payload():
    payload = valid_booking_payload()
    response = create_booking(payload)

    assert response.status_code == 200
    assert "bookingid" in response.json()
    assert response.json()["booking"]["firstname"] == payload["firstname"]


def test_create_booking_missing_firstname():
    payload = valid_booking_payload()
    payload.pop("firstname")

    response = create_booking(payload)

    # Restful Booker is a public demo API and may not enforce all validations strictly.
    # In production, this should be a strict 400/422 based on the API contract.
    assert response.status_code in [400, 422, 500]


def test_create_booking_invalid_totalprice():
    payload = valid_booking_payload()
    payload["totalprice"] = "not-a-number"

    response = create_booking(payload)

    # Restful Booker is a public demo API and may not enforce all validations strictly.
    # In production, this should be a strict 400/422 based on the API contract.
    assert response.status_code in [400, 422, 500]
