# Booking API Context

This file represents the retrieved context that an AI system would use before generating BDD scenarios.

## Booking Creation Endpoint

POST /booking

Expected booking payload:

```json
{
  "firstname": "Jim",
  "lastname": "Brown",
  "totalprice": 111,
  "depositpaid": true,
  "bookingdates": {
    "checkin": "2026-01-01",
    "checkout": "2026-01-05"
  },
  "additionalneeds": "Breakfast"
}
```

Important fields:
- firstname
- lastname
- totalprice
- depositpaid
- bookingdates.checkin
- bookingdates.checkout

Useful negative validation ideas:
- missing firstname
- missing lastname
- invalid totalprice
- missing bookingdates
- checkout before checkin
- malformed JSON
