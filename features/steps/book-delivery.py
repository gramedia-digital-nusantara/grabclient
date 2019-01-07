from http import HTTPStatus
from unittest.mock import MagicMock

from behave import when, given, then
from behave.runner import Context
from requests import Response

from grabclient import GrabClient, DeliveryRequest, ServiceType, CashOnDelivery, Sender, Recipient, Origin, Coordinates, \
    Destination


@given('a simulated DeliveryRequest request')
def step_impl(context):
    context.simulated_request = DeliveryRequest(
        merchant_order_id='merchant order id',
        service_type=ServiceType.same_day,
        packages=[],
        cash_on_delivery=CashOnDelivery(amount=0),
        sender=Sender(first_name='first',
                      last_name='last',
                      title='employee',
                      company_name='company',
                      email='first@last.company',
                      phone='phone',
                      sms_enabled=True,
                      instruction=''),
        recipient=Recipient(first_name='first',
                      last_name='last',
                      title='employee',
                      company_name='company',
                      email='first@last.company',
                      phone='phone',
                      sms_enabled=True,
                      instruction=''),
        origin=Origin(address='Full address of origin',
                 keywords='Extra keywords',
                 coordinates=Coordinates(latitude=1.1, longitude=1.2)),
        destination=Destination(address='Full address of customer',
                                keywords='Extra keywords',
                                coordinates=Coordinates(latitude=1.1, longitude=1.2))
    )


@then("the response is deserialized correctly for a DeliveryResponse")
def step_impl(context: Context):
    assert context.response.delivery_id == 'string'
    assert context.response.merchant_order_id == 'string'
    assert context.response.tracking_url == 'string'


@when("I perform book delivery")
def step_impl(context):
    client: GrabClient = context.client

    mock = MagicMock(spec=Response)
    mock.json = lambda: context.simulated_json

    context.requests_mock.post.return_value = mock
    context.requests_mock.post.return_value.status_code = HTTPStatus.OK

    context.response = client.book_delivery(
        DeliveryRequest(
            merchant_order_id='merchant order id',
            service_type=ServiceType.same_day,
            packages=[],
            cash_on_delivery=CashOnDelivery(amount=0),
            sender=Sender(first_name='first',
                          last_name='last',
                          title='employee',
                          company_name='company',
                          email='first@last.company',
                          phone='phone',
                          sms_enabled=True,
                          instruction=''),
            recipient=Recipient(first_name='first',
                                last_name='last',
                                title='employee',
                                company_name='company',
                                email='first@last.company',
                                phone='phone',
                                sms_enabled=True,
                                instruction=''),
            origin=Origin(address='Full address of origin',
                          keywords='Extra keywords',
                          coordinates=Coordinates(latitude=1.1, longitude=1.2)),
            destination=Destination(address='Full address of customer',
                                    keywords='Extra keywords',
                                    coordinates=Coordinates(latitude=1.1, longitude=1.2))
        )
    )
