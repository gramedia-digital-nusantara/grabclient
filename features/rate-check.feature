Feature: Rate Checking
    getting an estimated shipping cost.

    Scenario: Request Serialization
        Given a simulated DeliveryQuoteRequest request
        When I serialize the request
        Then the request is serialized correctly for /deliveries/quotes

    Scenario: Response Deserialization
        Given a simulated response from /deliveries/quotes
        And a simulated DeliveryQuoteRequest request
        When I deserialize the response as DeliveryQuoteResponse
        Then the response is deserialized correctly for a DeliveryQuote

    Scenario: Checking Shipping Rate via Client
        Given a production API client
        And a simulated response from /deliveries/quotes
        When I perform a rate lookup
        Then the request is a POST made to https://api.grab.com/v1/deliveries/quotes
#        And the request credentials are set properly
        And the response is deserialized correctly for a DeliveryQuote
