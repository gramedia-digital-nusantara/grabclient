import base64
import hashlib
import hmac
import json
from enum import Enum
from http import HTTPStatus
from unittest.mock import MagicMock

from behave import given, when, then
from behave.runner import Context
from requests import Response

from grabclient import GrabClient
from grabclient.exceptions import APIErrorResponse
from grabclient.responses import AbstractDeserializableResponse, DeliveryQuoteResponse, DeliveryResponse


class SimulationType(Enum):
    request = 'request'
    response = 'response'


SIMULATED_JSON = {
    '/deliveries/quote': {
        SimulationType.response: {
            "quotes": [
                {
                    "service": {
                        "id": 0,
                        "name": "string"
                    },
                    "currency": {
                        "code": "SGD",
                        "symbol": "string",
                        "exponent": 0
                    },
                    "amount": 0,
                    "estimatedTimeline": {
                        "create": "string",
                        "allocate": "string",
                        "pickup": "string",
                        "dropoff": "string",
                        "cancel": "string",
                        "return": "string"
                    },
                    "distance": 0
                }
            ],
            "packages": [
                {
                    "name": "string",
                    "description": "string",
                    "quantity": 0,
                    "price": 0,
                    "insuranceValue": 0,
                    "insuranceType": "BASIC",
                    "currency": {
                        "code": "SGD",
                        "symbol": "string",
                        "exponent": 0
                    },
                    "dimensions": {
                        "height": 0,
                        "width": 0,
                        "depth": 0,
                        "weight": 0
                    }
                }
            ],
            "origin": {
                "address": "string",
                "keywords": "string",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "extra": {}
            },
            "destination": {
                "address": "string",
                "keywords": "string",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "extra": {}
            }
        },
        SimulationType.request: {
            "packages": [
                {
                    "name": "string",
                    "description": "string",
                    "quantity": 0,
                    "price": 0,
                    "insuranceValue": 0,
                    "insuranceType": "BASIC",
                    "currency": {
                        "code": "SGD",
                        "symbol": "string",
                        "exponent": 0
                    },
                    "dimensions": {
                        "height": 0,
                        "width": 0,
                        "depth": 0,
                        "weight": 0
                    }
                }
            ],
            "origin": {
                "address": "string",
                "keywords": "string",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "extra": {}
            },
            "destination": {
                "address": "string",
                "keywords": "string",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "extra": {}
            }
        }
    },
    '/deliveries': {
        SimulationType.request: {
            "merchantOrderID": "string",
            "serviceType": "INSTANT",
            "packages": [
                {
                    "name": "string",
                    "description": "string",
                    "quantity": 0,
                    "price": 0,
                    "dimensions": {
                        "height": 0,
                        "width": 0,
                        "depth": 0,
                        "weight": 0
                    }
                }
            ],
            "cashOnDelivery": {
                "amount": 0
            },
            "sender": {
                "firstName": "string",
                "lastName": "string",
                "title": "string",
                "companyName": "string",
                "email": "string",
                "phone": "string",
                "smsEnabled": True,
                "instruction": "string"
            },
            "recipient": {
                "firstName": "string",
                "lastName": "string",
                "title": "string",
                "companyName": "string",
                "email": "string",
                "phone": "string",
                "smsEnabled": True,
                "instruction": "string"
            },
            "origin": {
                "address": "string",
                "keywords": "string",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "extra": {

                }
            },
            "destination": {
                "address": "string",
                "keywords": "string",
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "extra": {

                }
            }
        },
        SimulationType.response: {
            "deliveryID": "string",
            "merchantOrderID": "string",
            "quote": {
                "service": {
                    "id": 0,
                    "name": "string"
                },
                "currency": {
                    "code": "SGD",
                    "symbol": "string",
                    "exponent": 0
                },
                "amount": 0,
                "estimatedTimeline": {
                    "create": "string",
                    "allocate": "string",
                    "pickup": "string",
                    "dropoff": "string",
                    "cancel": "string",
                    "return": "string"
                },
                "distance": 0,
                "packages": [
                    {
                        "name": "string",
                        "description": "string",
                        "quantity": 0,
                        "price": 0,
                        "dimensions": {
                            "height": 0,
                            "width": 0,
                            "depth": 0,
                            "weight": 0
                        }
                    }
                ],
                "origin": {
                    "address": "string",
                    "keywords": "string",
                    "coordinates": {
                        "latitude": 0,
                        "longitude": 0
                    },
                    "extra": {}
                },
                "destination": {
                    "address": "string",
                    "keywords": "string",
                    "coordinates": {
                        "latitude": 0,
                        "longitude": 0
                    },
                    "extra": {}
                }
            },
            "sender": {
                "firstName": "string",
                "lastName": "string",
                "title": "string",
                "companyName": "string",
                "email": "string",
                "phone": "string",
                "smsEnabled": True,
                "instruction": "string"
            },
            "recipient": {
                "firstName": "string",
                "lastName": "string",
                "title": "string",
                "companyName": "string",
                "email": "string",
                "phone": "string",
                "smsEnabled": True,
                "instruction": "string"
            },
            "pickupPin": "string",
            "status": "ALLOCATING",
            "courier": {
                "coordinates": {
                    "latitude": 0,
                    "longitude": 0
                },
                "name": "string",
                "phone": "string",
                "pictureURL": "string",
                "vehicle": {
                    "plateNumber": "string",
                    "model": "string"
                }
            },
            "timeline": {
                "create": "string",
                "allocate": "string",
                "pickup": "string",
                "dropoff": "string",
                "cancel": "string",
                "return": "string"
            },
            "trackingURL": "string",
            "advanceInfo": {
                "failedReason": "string"
            }
        }
    }
}


@given('a production API client')
def step_impl(context: Context) -> None:
    context.client = GrabClient(
        credentials=('client_id', 'secret'),
        sandbox_mode=False
    )


@given('using a simulated {resp} response from {endpoint}')
def step_impl(context: Context, resp: str, endpoint: str) -> None:
    try:
        context.simulated_json = SIMULATED_JSON[endpoint][resp]

        mock = MagicMock(spec=Response)
        mock.json = lambda: context.simulated_json

        context.requests_mock.post.return_value = mock
    except APIErrorResponse as e:
        pass
    except KeyError:
        raise RuntimeError(
            f'Misconfigured test: No simulated responses for "{endpoint}"')


@then("the request is serialized correctly for {endpoint}")
def step_impl(context: Context, endpoint: str) -> None:
    expected_json = SIMULATED_JSON[endpoint][SimulationType.request]
    actual_json = json.loads(context.serialized_request)
    assert dict_diff(expected_json, actual_json)


@given('a simulated response from {endpoint}')
def step_impl(context: Context, endpoint: str) -> None:
    try:
        context.simulated_json = SIMULATED_JSON[endpoint][SimulationType.response]
    except KeyError:
        raise RuntimeError(f'Misconfigured test: No simulated responses for "{endpoint}"')


@when('I deserialize the response as {class_name}')
def step_impl(context: Context, class_name: str) -> None:
    try:
        cls: AbstractDeserializableResponse = {
            'DeliveryQuoteResponse': DeliveryQuoteResponse,
            'DeliveryResponse': DeliveryResponse,
        }[class_name]
        context.response = cls.from_api_json(context.simulated_json)
    except KeyError:
        raise RuntimeError(f'Misconfigured test: Unknown class "{class_name}"')


KEYNOTFOUND = '<KEYNOTFOUND>'  # KeyNotFound for dictDiff


def dict_diff(first, second):
    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by KEYNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    # Check all keys in first dict
    for key in first.keys():
        if not key in second:
            diff[key] = (first[key], KEYNOTFOUND)
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second.keys():
        if not key in first:
            diff[key] = (KEYNOTFOUND, second[key])
    return diff


@then('the request credentials for {method} mode are set properly to {url}')
def step_impl(context: Context, method: str, url: str) -> None:
    call = context.requests_mock.post.call_args
    headers = call[1]['headers']
    auth = headers['Authorization']
    h = hashlib.sha256()
    h.update(call[1]['data'].encode('ascii'))
    string_to_sign = method + '\n' + headers['Content-Type'] + '\n' + headers[
        'Date'] + '\n' + url + '\n' + base64.b64encode(h.digest()).decode() + '\n'

    hmac_signature = hmac.new('secret'.encode(), string_to_sign.encode(), hashlib.sha256).digest()
    hmac_signature_encoded: object = base64.b64encode(hmac_signature)
    assert f'client_id:{hmac_signature_encoded}' == auth


@when('I serialize the request')
def step_impl(context):
    c = GrabClient(('client_id', 'secret'), False)
    context.serialized_request = c._serialize_request(
        context.simulated_request)


@then('the response is properly deserialized')
def step_impl(context: Context):
    response = context.response


@then('the request is a {method} made to {url}')
def step_impl(context: Context, method: str, url: str) -> None:
    call = context.requests_mock.post.call_args
    assert call[0][0] == url



