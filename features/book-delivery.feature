Feature: Delivery Scheduling
  This is the main use of the Grab Client.  Delivery scheduling
  (more correctly called 'Pickup Scheduling') is how a client informs
  Grab they have a package that needs picked-up and delivered to a client.
  Within this library, we refer to it as 'Delivery Scheduling' to keep the
  terminology in line with what is states in Grab's API documentation.

  Scenario: Request Serialization
    Given a simulated DeliveryRequest request
    When I serialize the request
    Then the request is serialized correctly for /v1/deliveries

  Scenario: Response Deserialization
    Given a simulated response from /v1/deliveries
    When I deserialize the response as DeliveryResponse
    Then the response is deserialized correctly for a DeliveryResponse

  Scenario: Book Delivery via Client
    Given a production API client
    And a simulated response from /v1/deliveries
    When I perform book delivery
    Then the request is a POST made to https://api.grab.com/v1/deliveries
    And the request credentials for POST mode are set properly to /v1/deliveries
    And the response is deserialized correctly for a DeliveryResponse
