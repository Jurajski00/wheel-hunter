from dataclasses import dataclass, field
from enum import StrEnum

class FuelType(StrEnum):
    PETROL_LPG = "petrol + lpg"
    PETROL = "petrol"
    DIESEL = "diesel"


class BodyType(StrEnum):
    HATCHBACK = "hatchback"
    SEDAN = "sedan"
    KOMBI = "kombi"
    SUV = "suv"
    COUPE = "coupe"
    CONVERTIBLE = "convertible"
    MINIVAN = "minivan"


class SellerType(StrEnum):
    PRIVATE = "private"
    DEALER = "dealer"


@dataclass
class Car:
    identifier: int = field(init = False)
    score: int = field(init = False)

    brand: str
    model: str
    year: int
    price: int
    mileage: int
    fuel_type: FuelType
    gearbox: str
    horsepower: int
    displacement: int
    body_type: BodyType
    location: str
    seller_type: SellerType
    source: str
    url: str