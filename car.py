from dataclasses import dataclass, field

@dataclass
class Car:
    identifier: int = field(init=False)
    brand: str
    model: str
    year: int
    price: int
    mileage: int
    url: str