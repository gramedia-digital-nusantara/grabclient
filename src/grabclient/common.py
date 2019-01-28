from enum import Enum
from typing import NamedTuple, List

__all__ = ['CurrencyCode', 'InsuranceType', 'Coordinates', 'Dimensions', 'Currency', 'Package', 'Origin', 'Destination']


class CurrencyCode(Enum):
    sgd = "SGD"
    php = "PHP"
    myr = "MYR"
    vnd = "VND"
    thb = "THB"
    idr = "IDR"


class ServiceType(Enum):
    instant = "INSTANT"
    same_day = "SAME_DAY"


class InsuranceType(Enum):
    basic = "BASIC"
    premium = "PREMIUM"


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class Dimensions(NamedTuple):
    height: int
    width: int
    depth: int
    weight: int


class Currency(NamedTuple):
    """

    """
    code: CurrencyCode  # [SGD, PHP, MYR, VND, THB, IDR]
    symbol: str = "string"
    exponent: int = 0


class Package(NamedTuple):
    name: str
    description: str
    quantity: int
    price: int
    currency: Currency
    dimensions: Dimensions
    # insurance_value: int = 0
    # insurance_type: InsuranceType = InsuranceType.basic


class DestinationClass(NamedTuple):
    address: str
    keywords: str
    coordinates: Coordinates
    extra: dict = {}


class Origin(DestinationClass):
    pass


class Destination(DestinationClass):
    pass


class Service(NamedTuple):
    id: int
    name: str


class EstimatedTimeline(NamedTuple):
    create: str
    allocate: str
    pickup: str
    dropoff: str
    cancel: str
    returns: str


class QuoteParam(NamedTuple):
    service: Service
    currency: Currency
    amount: int
    estimated_timeline: EstimatedTimeline
    distance: int


QuoteList = List[QuoteParam]


class Quotes(NamedTuple):
    quotes: List[QuoteParam]
    packages: List[Package]


class Contact(NamedTuple):
    first_name: str
    last_name: str
    title: str
    company_name: str
    email: str
    phone: str
    sms_enabled: bool = True
    instruction: str = ''


class Sender(Contact):
    pass


class Recipient(Contact):
    pass


class CashOnDelivery(NamedTuple):
    amount: int = 0


class Vehicle(NamedTuple):
    plate_number: str
    model: str


class StatusType(Enum):
    allocating = "ALLOCATING"
    picking_up = "PICKING_UP"
    in_delivery = "IN_DELIVERY"
    in_return = "IN_RETURN"
    completed = "COMPLETED"
    cancelled = "CANCELED"
    returned = "RETURNED"
    failed = "FAILED"


class AdvancedInfo(NamedTuple):
    failed_reason: str


class Quote(QuoteParam):
    packages: List[Package]
    origin: Origin
    destination: Destination


class Courier(NamedTuple):
    coordinates: Coordinates
    name: str
    phone: str
    picture_url: str
    vehicle: Vehicle
