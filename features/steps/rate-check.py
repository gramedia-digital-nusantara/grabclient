from http import HTTPStatus
from unittest.mock import MagicMock

from behave import given, when, then
from requests import Response

from grabclient import DeliveryQuoteRequest, Origin, Destination, Coordinates, GrabClient, Package, Currency, Dimensions


@then("the response is deserialized correctly for a DeliveryQuote")
def step_impl(context):
    assert len(context.response.quotes) == 1
    assert len(context.response.packages) == 1



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


@when('I perform a rate lookup')
def step_impl(context):
    client: GrabClient = context.client

    mock = MagicMock(spec=Response)
    mock.json = lambda: context.simulated_json

    context.requests_mock.post.return_value = mock
    context.requests_mock.post.return_value.status_code = HTTPStatus.OK

    context.response = client.check_rate(
        DeliveryQuoteRequest(
            packages=[Package(name="string",
                              description="string",
                              quantity=0,
                              price=0,
                              currency= Currency(code= "SGD",
                                                 symbol= "string",
                                                 exponent=0),
                              dimensions= Dimensions(height=0,
                                                     width=0,
                                                     depth=0,
                                                     weight=0)
                              )],
            origin=Origin(address='string',
                          keywords='string',
                          coordinates=Coordinates(latitude=0, longitude=0),
                          extra={}),
            destination=Destination(address='string',
                                    keywords='string',
                                    coordinates=Coordinates(latitude=0, longitude=0),
                                    extra={})
        )
    )
