from abc import ABCMeta, abstractmethod
from typing import List

from grabclient.common import Origin, Package, Destination, ServiceType, CashOnDelivery, Sender, Recipient

class AbstractDeserializableRequest(metaclass=ABCMeta):
    """ Essentially the base class for all API responses.  This just defines __slots__
    and ensures that all derived classes need to define a from_api_json class method.
    """
    __slots__ = ()

    @classmethod
    @abstractmethod
    def to_api_json(cls):
        pass


class DeliveryQuoteRequest(AbstractDeserializableRequest):
    __slots__ = (
        'packages', 'origin', 'destination'
    )

    def __init__(self,
                 packages: List[Package],
                 origin: Origin,
                 destination: Destination):
        self.origin = origin
        self.destination = destination
        self.packages = packages

    @classmethod
    def to_api_json(cls):
        return cls(
            origin=cls.origin,
            destination=cls.destination,
            packages=cls.packages
        )


class ScheduleDeliveryRequest:
    __slots__ = (
        'merchant_order_id',
        'service_type',
        'packages',
        'cash_on_delivery',
        'sender',
        'recipient',
        'origin',
        'destination'
    )

    def __init__(self,
                 merchant_order_id: str,
                 service_type: ServiceType,
                 packages: List[Package],
                 cash_on_delivery: CashOnDelivery,
                 sender: Sender,
                 recipient: Recipient,
                 origin: Origin,
                 destination: Destination):
        self.merchant_order_id = merchant_order_id
        self.service_type = service_type
        self.packages = packages
        self.cash_on_delivery = cash_on_delivery
        self.sender = sender
        self.recipient = recipient
        self.origin = origin
        self.destination = destination
