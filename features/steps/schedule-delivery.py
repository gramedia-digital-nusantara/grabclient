# from datetime import datetime, timezone
# from unittest.mock import MagicMock
#
# from behave import given, then, when
# from behave.runner import Context
# from requests import Response
#
# from grabclient import GrabClient, CashOnDelivery
# from grabclient.common import ServiceType
# from grabclient.requests import ScheduleDeliveryRequest, Sender, Recipient, Origin, Destination, Package
#
#
# @then("the response is deserialized correctly for a DeliveryScheduledResponse")
# def step_impl(context: Context):
#     assert context.response.status == 'OK'
#     assert context.response.order_number == 'EDS12345678'
#     assert context.response.web_order_id == '12345678'
#     assert context.response.label_url == 'http://api.staging.etobee.com/api/print_label?order_number=EDS67455165'
#     assert context.response.message == 'Booking in progress'
#
#
# @given("a simulated ScheduleDeliveryRequest request")
# def step_impl(context: Context):
#     context.simulated_request = ScheduleDeliveryRequest(
#         merchant_order_id='',
#         service_type=ServiceType.same_day,
#         packages=[],
#         cash_on_delivery=CashOnDelivery(amount=0),
#         sender=Sender(),
#         recipient=Recipient(),
#         origin=Origin(),
#         destination=Destination()
#     )
#
#
# @when("I perform a delivery schdedulling")
# def step_impl(context):
#     client: GrabClient = context.client
#
#     mock = MagicMock(spec=Response)
#     mock.json = lambda: context.simulated_json
#
#     context.requests_mock.post.return_value = mock
#
#     context.response = client.schedule_delivery(
#         ScheduleDeliveryRequest(
#             web_order_id='12345678',
#             sender=Person(
#                 name='Angela',
#                 mobile='+62 87654321',
#                 email='angela@example.com'
#             ),
#             origin=Address(
#                 address='Jl. Kebagusan 1',
#                 city='Jakarta Barat',
#                 state='Jakarta Barat',
#                 country='Indonesia',
#                 postcode='11410'
#             ),
#             origin_comments='Use the side door',
#             recipient=Person(
#                 name='Sven',
#                 mobile='+62 12345678',
#                 email='sven@example.com'
#             ),
#             destination=Address(
#                 address='Jl. Kebagusan 10',
#                 city='Jakarta Barat',
#                 state='Jakarta Barat',
#                 country='Indonesia',
#                 postcode='11410'
#             ),
#             package=Package(
#                 quantity=1,
#                 transaction_value=100000,
#                 item_full_price=120000,
#                 insurance=False,
#                 photo='http://www.flickr.com/bird.jpg',
#                 size='Motorcycle',
#                 weight=1,
#                 volume=0.1,
#                 note='Fragile',
#                 width=1,
#                 height=1,
#                 length=1,
#                 locker_dropoff=False
#             ),
#             merchant_id='MRCHNT-123',
#             paid_by_parent=False,
#             is_cod=False,
#             pickup_time=datetime(year=2016, month=10, day=2, hour=10, tzinfo=timezone.utc),
#             pickup_type=PickupType.next_day_service,
#             destination_comments='Call 123 if nobody is in.'
#         )
#     )
