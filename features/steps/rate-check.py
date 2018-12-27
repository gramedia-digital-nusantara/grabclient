from behave import given, when, then

from grabclient import DeliveryQuoteRequest, Origin, Destination, Coordinates, GrabClient


@then("the response is deserialized correctly for a DeliveryQuote")
def step_impl(context):
    assert len(context.response.quotes) == 1


@given('a simulated DeliveryQuoteRequest request')
def step_impl(context):
    context.simulated_request = DeliveryQuoteRequest(
        packages=[],
        origin=Origin(address='Full address of origin',
                      keywords='Extra keywords',
                      coordinates=Coordinates(latitude=1.1, longitude=1.2)),
        destination=Destination(address='Full address of customer',
                                keywords='Extra keywords',
                                coordinates=Coordinates(latitude=1.1, longitude=1.2))
    )


@when('I serialize the request')
def step_impl(context):
    c = GrabClient(('client_id', 'secret'), False)
    context.serialized_request = c._serialize_request(
        context.simulated_request)
