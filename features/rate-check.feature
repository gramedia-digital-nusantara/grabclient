Feature: Rate Checking
    getting an estimated shipping cost.

    Scenario: Request Serialization
        Given a simulated DeliveryQuoteRequest request
        When I serialize the request
        Then the request is serialized correctly for /deliveries/quote

    Scenario: Response Deserialization
        Given a simulated response from /deliveries/quote
        And a simulated DeliveryQuoteRequest request
        When I deserialize the response as DeliveryQuoteResponse
        Then the response is deserialized correctly for a DeliveryQuote
#
#    Scenario: Checking Shipping Rate via Client
#        Given using a simulated authorized response from auth
#        And a production API client
#        And a simulated CheckRateRequest request
#        And a simulated response from tarif/product
#        When I perform a rate lookup
#        Then the request is a POST made to http://apis.mytiki.net/check_rate
#        And the request credentials are set properly
#        And the response is deserialized correctly for a RateEstimate
