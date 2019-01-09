from abc import ABCMeta, abstractmethod
from typing import NamedTuple, List

from grabclient.common import QuoteParam, Package, Origin, Destination, Quote, Sender, Recipient, StatusType, Courier, \
    EstimatedTimeline, AdvancedInfo


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
                 quotes: List[QuoteParam],
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


class DeliveryResponse(AbstractDeserializableResponse):
    __slots__ = (
        'delivery_id', 'merchant_order_id', 'quote', 'sender',
        'recipient', 'pickup_pin', 'status', 'courier', 'timeline',
        'tracking_url', 'advanced_info'
    )

    def __init__(self,
                 delivery_id: str,
                 merchant_order_id: str,
                 quote: Quote,
                 sender: Sender,
                 recipient: Recipient,
                 pickup_pin: str,
                 status: StatusType,
                 courier: Courier,
                 timeline: EstimatedTimeline,
                 tracking_url: str,
                 advanced_info: AdvancedInfo):
        self.delivery_id = delivery_id
        self.merchant_order_id = merchant_order_id
        self.quote = quote
        self.sender = sender
        self.recipient = recipient
        self.pickup_pin = pickup_pin
        self.status = status
        self.courier = courier
        self.timeline = timeline
        self.tracking_url = tracking_url
        self.advanced_info = advanced_info

    @classmethod
    def from_api_json(cls, api_json: dict):
        return cls(
            delivery_id=api_json.get('deliveryID'),
            merchant_order_id=api_json.get('merchantOrderID'),
            quote=api_json.get('quote'),
            sender=api_json.get('sender'),
            recipient=api_json.get('recipient'),
            pickup_pin=api_json.get('pickupPin'),
            status=api_json.get('status'),
            courier=api_json.get('courier'),
            timeline=api_json.get('timeline'),
            tracking_url=api_json.get('trackingURL'),
            advanced_info=api_json.get('advancedInfo')
        )
