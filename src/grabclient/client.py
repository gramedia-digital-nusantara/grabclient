import base64
import hashlib
import hmac
import json
from collections import namedtuple
from datetime import datetime
from enum import Enum
from http import HTTPStatus
from typing import Tuple, Union, TypeVar, Type

import requests

from grabclient.exceptions import APINotContactable, APIResponseNotJson, APIErrorResponse
from grabclient.helper import snake_to_camel
from grabclient.requests import DeliveryQuoteRequest, DeliveryRequest
from grabclient.responses import DeliveryQuoteResponse, DeliveryResponse

__all__ = ['GrabClient', ]

T = TypeVar('T')


class GrabClient:

    def __init__(self, credentials: Tuple[str, str], sandbox_mode=False):
        self.credentials = credentials
        self.sandbox_mode = sandbox_mode

    @property
    def verify_ssl(self):
        """

        :return:
        """
        return not self.sandbox_mode

    @property
    def base_url(self):
        """

        :return:
        """
        return 'https://api.stg-myteksi.com/v1' if self.sandbox_mode else 'https://api.grab.com/v1'

    def check_rate(self, req: DeliveryQuoteRequest) -> DeliveryQuoteResponse:
        """POST /deliveries/quotes"""
        return self._http_post_json('/deliveries/quotes', req, DeliveryQuoteResponse)

    def book_delivery(self, req: DeliveryRequest) -> DeliveryResponse:
        """Booking API: POST /deliveries"""
        return self._http_post_json('/deliveries', req, DeliveryResponse)

    def track_delivery(self):
        """Tracking API: GET /deliveries/{deliveryID}/tracking tyg"""
        pass

    def cancel_delivery(self, delivery_id: str):
        """Cancel API: /deliveries/{deliveryID}"""
        return self._http_delete_json(f'/deliveries/{delivery_id}')

    def info_delivery(self, delivery_id: str) -> DeliveryResponse:
        """GET deliveries/{DeliveryID}"""
        return self._http_get_json(f'/deliveries/{delivery_id}', DeliveryResponse)

    def _headers(self):
        return {
            'Accept': 'application/json',
            'Date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        }

    def _http_get_json(self, url_path: str, response_class: Type[T]) -> T:
        """
        :param url_path:
        :param response_class:
        :return:
        """
        headers = self._headers()
        headers['Content-Type'] = ""
        headers['Authorization'] = self.calculate_hash('', url_path, headers, 'GET')
        try:
            http_response = requests.get(
                f"{self.base_url}{url_path}",
                headers=headers
            )
            if http_response.status_code is not HTTPStatus.OK:
                raise APIErrorResponse.from_api_json(http_response=http_response)
            return response_class.from_api_json(http_response.json())
        except Exception as e:
            raise Exception from e
        except requests.RequestException as e:
            raise APINotContactable from e
        except ValueError as e:
            raise APIResponseNotJson from e

    def _http_post_json(self, url_path: str, payload: Union[dict, namedtuple], response_class: Type[T]) -> T:
        """

        :param url_path:
        :param payload:
        :param response_class:
        :return:
        """
        headers = self._headers()
        headers['Content-Type'] = 'application/json'
        data = self._serialize_request(payload)
        headers['Authorization'] = self.calculate_hash(data, url_path, headers, 'POST')
        try:
            http_response = requests.post(
                f"{self.base_url}{url_path}",
                headers=headers,
                data=data
            )
            if http_response.status_code is not HTTPStatus.OK:
                raise APIErrorResponse.from_api_json(http_response=http_response)
            return response_class.from_api_json(http_response.json())
        except requests.RequestException as e:
            raise APINotContactable from e
        except ValueError as e:
            raise APIResponseNotJson from e

    def _http_delete_json(self, url_path: str):
        """
        :param url_path:
        :param response_class:
        :return:
        """
        headers = self._headers()
        headers['Content-Type'] = ""
        headers['Authorization'] = self.calculate_hash('', url_path, headers, 'DELETE')
        try:
            http_response = requests.delete(
                f"{self.base_url}{url_path}",
                headers=headers
            )
            if http_response.status_code is not HTTPStatus.NO_CONTENT:
                raise APIErrorResponse.from_api_json(http_response=http_response)
            return http_response
        except Exception as e:
            raise Exception from e
        except requests.RequestException as e:
            raise APINotContactable from e
        except ValueError as e:
            raise APIResponseNotJson from e

    def _marshal_request(self, payload) -> dict:
        """

        :param payload:
        :return:
        """
        marshalled = {}
        # 1. Skip all non-public attributes (starts with sunder or dunder)
        # 2. special case to ignore 'index' and 'count' attributes for namedtuples
        for attr_name in [a for a in dir(payload)
                          if not a.startswith('_') and a not in ('index', 'count')]:
            attr_val = getattr(payload, attr_name)
            cameled_attr_name = snake_to_camel(attr_name)
            if isinstance(attr_val, datetime):
                marshalled[cameled_attr_name] = int(attr_val.timestamp())
            elif isinstance(cameled_attr_name, Enum):
                marshalled[cameled_attr_name] = attr_val.value
            elif isinstance(attr_val, (int, str, bool, float)):
                marshalled[cameled_attr_name] = attr_val
            else:
                marshalled[cameled_attr_name] = self._marshal_request(attr_val)
        return marshalled

    def _serialize_request(self, payload) -> str:
        """

        :param payload:
        :return:
        """
        return json.dumps(self._marshal_request(payload))

    def calculate_hash(self, data: str, url: str, headers: dict, method: str):
        """

        :param data:
        :param url:
        :param headers:
        :param method:
        :return:
        """
        client_id, secret = self.credentials

        h = hashlib.sha256()
        h.update(data.encode('ascii'))
        string_to_sign = method + '\n' + headers['Content-Type'] + '\n' + headers[
            'Date'] + '\n' + url + '\n' + base64.b64encode(h.digest()).decode() + '\n'

        hmac_signature = hmac.new(secret.encode(), string_to_sign.encode(), hashlib.sha256).digest()
        hmac_signature_encoded: object = base64.b64encode(hmac_signature)

        return f'{client_id}:{hmac_signature_encoded}'
