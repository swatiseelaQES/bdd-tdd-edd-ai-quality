from behave import given, when, then
from src.booking_client import create_booking, valid_booking_payload


@given("I have a valid booking request")
def step_have_valid_booking_request(context):
    context.payload = valid_booking_payload()


@when("I remove the firstname field")
def step_remove_firstname(context):
    context.payload.pop("firstname", None)


@when("I set totalprice to a non-numeric value")
def step_set_invalid_totalprice(context):
    context.payload["totalprice"] = "not-a-number"


@when("I set checkout before checkin")
def step_set_checkout_before_checkin(context):
    context.payload["bookingdates"]["checkin"] = "2026-01-05"
    context.payload["bookingdates"]["checkout"] = "2026-01-01"


@when("I send a POST request to /booking")
def step_send_post_request(context):
    context.response = create_booking(context.payload)


@then("the booking should be created successfully")
def step_booking_should_be_created(context):
    assert context.response.status_code == 200
    body = context.response.json()

    assert "bookingid" in body
    assert body["booking"]["firstname"] == context.payload["firstname"]


@then("the API should reject the request")
def step_api_should_reject_request(context):
    # Restful Booker is a public demo API and may not enforce all validations strictly.
    # In a real API, this should be tightened to the exact expected status code.
    assert context.response.status_code in [400, 422, 500]
