from typing import List

from grabclient.common import Origin, Package, Destination, ServiceType, CashOnDelivery, Sender, Recipient


class DeliveryQuoteRequest:
    __slots__ = (
        'service_type', 'packages', 'origin', 'destination'
    )

    def __init__(self,
                 service_type: ServiceType,
                 packages: List[Package],
                 origin: Origin,
                 destination: Destination):
        self.service_type = service_type
        self.origin = origin
        self.destination = destination
        self.packages = packages


class DeliveryRequest:
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
