from car import Car

MAX_PRICE_SCORE = 35
MAX_MILEAGE_SCORE = 30
FULE_TYPE_SCORES = {
    "petrol + lpg": 15,
    "petrol": 8,
    "diesel": 0
}
MAX_HORSEPOWER_SCORE = 10
SELLER_TYPE_SCORES = {
    "private": 5,
    "dealer": 0
}
MAX_YEAR_SCORE = 5

MAX_ACCEPTABLE_PRICE = 20000
MIN_ACCEPTABLE_PRICE = 12000
MAX_ACCEPTABLE_MILEAGE = 200000
MIN_ACCEPTABLE_MILEAGE = 80000
MAX_ACCEPTABLE_HORSEPOWER = 180
MIN_ACCEPTABLE_HORSEPOWER = 100
MAX_ACCEPTABLE_YEAR = 2017
MIN_ACCEPTABLE_YEAR = 2010


def get_score(car: Car) -> int:
    return sum((
        price_scoring(car.price),
        mileage_scoring(car.mileage),
        fuel_type_scoring(car.fuel_type),
        horespower_scoring(car.horsepower),
        seller_type_scoring(car.seller_type),
        year_scoring(car.year)
    ))


def price_scoring(price: int) -> int:
    price = min(MAX_ACCEPTABLE_PRICE, max(price, MIN_ACCEPTABLE_PRICE))
    return round(MAX_PRICE_SCORE * ((MAX_ACCEPTABLE_PRICE - price) / (MAX_ACCEPTABLE_PRICE - MIN_ACCEPTABLE_PRICE)))


def mileage_scoring(mileage: int) -> int:
    mileage = min(MAX_ACCEPTABLE_MILEAGE, max(mileage, MIN_ACCEPTABLE_MILEAGE))
    return round(MAX_MILEAGE_SCORE * ((MAX_ACCEPTABLE_MILEAGE - mileage) / (MAX_ACCEPTABLE_MILEAGE - MIN_ACCEPTABLE_MILEAGE)))


def fuel_type_scoring(fuel_type: str) -> int:
    return FULE_TYPE_SCORES[fuel_type]


def horespower_scoring(horsepower: int) -> int:
    horsepower = min(MAX_ACCEPTABLE_HORSEPOWER, max(horsepower, MIN_ACCEPTABLE_HORSEPOWER))
    return round(MAX_HORSEPOWER_SCORE * ((horsepower - MIN_ACCEPTABLE_HORSEPOWER) / (MAX_ACCEPTABLE_HORSEPOWER - MIN_ACCEPTABLE_HORSEPOWER)))


def seller_type_scoring(seller_type: str) -> str:
    return SELLER_TYPE_SCORES[seller_type]


def year_scoring(year: int) -> int:
    year = min(MAX_ACCEPTABLE_YEAR, max(year, MIN_ACCEPTABLE_YEAR))
    return round(MAX_YEAR_SCORE * ((year - MIN_ACCEPTABLE_YEAR) / (MAX_ACCEPTABLE_YEAR - MIN_ACCEPTABLE_YEAR)))