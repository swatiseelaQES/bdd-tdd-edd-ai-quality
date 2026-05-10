Feature: Booking API validation
  As a tester
  I want booking API behavior to be described clearly
  So that expected behavior can be automated and evaluated

  Scenario: Create booking with a valid payload
    Given I have a valid booking request
    When I send a POST request to /booking
    Then the booking should be created successfully

  Scenario: Create booking with missing firstname
    Given I have a valid booking request
    When I remove the firstname field
    And I send a POST request to /booking
    Then the API should reject the request

  Scenario: Create booking with invalid totalprice
    Given I have a valid booking request
    When I set totalprice to a non-numeric value
    And I send a POST request to /booking
    Then the API should reject the request

  Scenario: Create booking with checkout before checkin
    Given I have a valid booking request
    When I set checkout before checkin
    And I send a POST request to /booking
    Then the API should reject the request
