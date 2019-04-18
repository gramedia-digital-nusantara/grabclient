Feature: Delivery Info
  This is the main use of the Grab Client.  Delivery info
  (more correctly called 'Info delivery') is how a client informs
  Grab they want to know information about delivery.
  Within this library, we refer to it as 'Delivery Info' to keep the
  terminology in line with what is states in Grab's API documentation.

  Scenario: Response Deserialization
    Given a simulated response from /v1/deliveries/string
    When I deserialize the response as DeliveryResponse
    Then the response is deserialized correctly for a DeliveryResponse

  Scenario: Delivery info via Client
    Given a production API client
    And a simulated response from /v1/deliveries/string
    When I perform request delivery info
    Then the request is a GET made to https://api.grab.com/v1/deliveries/string
    And the request credentials for GET mode are set properly to /v1/deliveries/string
    And the response is deserialized correctly for a DeliveryResponse
