import json
from enum import Enum
from http import HTTPStatus
from json import JSONDecodeError

from requests import Response


class APIExceptionType(Enum):
    api_exception = 'APIException'
    auth_exception = 'AuthException'
    forbidden_exception = 'ForbiddenException'
    create_exception = 'CreateException'
    fatal_exception = 'FatalException'
    limit_exception = 'LimitException'
    unknown_exception = 'UnknownException'


HTTPStatusMap = {
    400: APIExceptionType.api_exception,
    401: APIExceptionType.auth_exception,
    403: APIExceptionType.forbidden_exception,
    409: APIExceptionType.create_exception,
    429: APIExceptionType.limit_exception,
    500: APIExceptionType.fatal_exception
}


class GrabClientExceptionBase(Exception):
    """
    Base class for error
    """


class APINotContactable(GrabClientExceptionBase):
    """ Raised when the HTTP client cannot communicate with KGX.
    """

    def __init__(self, inner_exception):
        self.inner_exception = inner_exception

    def __str__(self):
        return str(self.inner_exception)


class APIResponseNotJson(GrabClientExceptionBase):
    """ Raised if the API response is not valid JSON.
    """

    def __init__(self, inner_exception):
        self.inner_exception = inner_exception

    def __str__(self):
        return str(self.inner_exception)


class APIErrorResponse(GrabClientExceptionBase):
    __slots__ = ('message', 'kind', 'code')

    def __init__(self, message: str, kind: APIExceptionType, code: HTTPStatus):
        self.message = message
        self.kind = kind
        self.code = code

    @classmethod
    def from_api_json(cls, http_response: Response):
        mapped_exception = HTTPStatusMap.get(http_response.status_code, None)
        if mapped_exception:
            try:
                message = json.loads(
                    http_response.content.decode('utf-8')
                ).get('message', '')
            except JSONDecodeError as e:
                message = ''
            return cls(
                message=message,
                kind=mapped_exception,
                code=http_response.status_code
            )

        return cls(
            message=http_response.content.decode('utf-8'),
            kind=APIExceptionType.unknown_exception,
            code=http_response.status_code
        )
