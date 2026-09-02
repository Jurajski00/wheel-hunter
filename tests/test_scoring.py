from scoring import price_scoring, get_score
import car
from pytest import fixture

def test_minimum_price_gets_max_score():
    result = price_scoring(12000)

    assert result == 35


@fixture
def honda_civic() -> car.Car:
    return car.Car(
        brand="Honda",
        model="Civic",
        year=2005,
        price=15000,
        mileage=90000,
        fuel_type=car.FuelType.PETROL,
        gearbox="automatic",
        horsepower=180,
        displacement=2000,
        body_type=car.BodyType.SUV,
        location="Siedlce",
        seller_type=car.SellerType.PRIVATE,
        source="olx",
        url="testurl"
    )

def test_car_gets_score(honda_civic):
    result = get_score(honda_civic)

    assert 0 <= result <= 100