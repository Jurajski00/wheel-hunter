from storage import get_id, save_car, get_cars
from car import Car

def add_car(car: Car) -> None:
    car.identifier = get_id()
    save_car(car)


def show_cars() -> list[dict]:
    return get_cars()