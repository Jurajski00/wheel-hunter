from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    year: int
    price: int
    mileage: int
    url: str