from http import HTTPStatus
from unittest.mock import MagicMock

from behave import when
from requests import Response

from grabclient import GrabClient


@when("I perform request delivery info")
def step_impl(context):
    client: GrabClient = context.client

    mock = MagicMock(spec=Response)
    mock.json = lambda: context.simulated_json

    context.requests_mock.get.return_value = mock
    context.requests_mock.get.return_value.status_code = HTTPStatus.OK

    context.response = client.info_delivery(delivery_id='string')
