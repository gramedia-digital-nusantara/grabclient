from abc import ABCMeta, abstractmethod
from typing import NamedTuple, List

from grabclient.common import Quote, Package, Origin, Destination


class AbstractDeserializableResponse(metaclass=ABCMeta):
    """ Essentially the base class for all API responses.  This just defines __slots__
    and ensures that all derived classes need to define a from_api_json class method.
    """
    __slots__ = ()

    @classmethod
    @abstractmethod
    def from_api_json(cls, api_json: dict):
        pass


class DeliveryQuoteResponse(AbstractDeserializableResponse):
    __slots__ = ('quotes', 'packages', 'origin', 'destination')

    def __init__(self,
                 quotes: List[Quote],
                 packages: List[Package],
                 origin: Origin,
                 destination: Destination):
        self.quotes = quotes
        self.packages = packages
        self.origin = origin
        self.destination = destination

    @classmethod
    def from_api_json(cls, api_json: dict):
        return cls(
            quotes=api_json.get('quotes', []),
            packages=api_json.get('packages', []),
            origin=api_json.get('origin'),
            destination=api_json.get('destination')
        )


# class ScheduleDeliveryResponse(AbstractDeserializableResponse):
#     __slots__ = (
#         'delivery_id', 'merchant_order_d',
#         'quote', 'sender', 'recipient',
#         'pickup_pin', 'status', 'courier', 'timeline',
#         'tracking_url', 'source_info'
#     )
#
#     def __init__(self,
#                  delivery_id: str):
