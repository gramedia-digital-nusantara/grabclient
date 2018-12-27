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
    insurance_value: int = 0
    insurance_type: InsuranceType = InsuranceType.basic


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


class Quote(NamedTuple):
    service: Service
    currency: Currency
    amount: int
    estimated_timeline: EstimatedTimeline
    distance: int


QuoteList = List[Quote]


class Quotes(NamedTuple):
    quotes: List[Quote]
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



