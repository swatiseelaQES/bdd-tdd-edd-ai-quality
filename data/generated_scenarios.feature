```gherkin
Feature: Booking Creation Negative Validation

  Scenario: Missing firstname in booking payload
    Given a booking payload without the "firstname" field
    When the client sends a POST request to /booking
    Then the response status code should be 400
    And the response should indicate "firstname" is required

  Scenario: Missing lastname in booking payload
    Given a booking payload without the "lastname" field
    When the client sends a POST request to /booking
    Then the response status code should be 400
    And the response should indicate "lastname" is required

  Scenario: Invalid totalprice as a negative number
    Given a booking payload with "totalprice" set to -50
    When the client sends a POST request to /booking
    Then the response status code should be 400
    And the response should indicate "totalprice" must be a positive number

  Scenario: Missing bookingdates object
    Given a booking payload without the "bookingdates" field
    When the client sends a POST request to /booking
    Then the response status code should be 400
    And the response should indicate "bookingdates" is required

  Scenario: Checkout date before checkin date
    Given a booking payload where "bookingdates.checkout" is before "bookingdates.checkin"
    When the client sends a POST request to /booking
    Then the response status code should be 400
    And the response should indicate "checkout" must be after "checkin"

  Scenario: Malformed JSON payload
    Given a malformed JSON payload
    When the client sends a POST request to /booking
    Then the response status code should be 400
    And the response should indicate invalid JSON format
```