from storage import save_car, get_cars, try_delete_car, get_next_id, get_car_score, sort_cars
from car import Car

def add_car(car: Car) -> None:
    car.identifier = get_next_id()
    car.score = get_car_score(car)
    save_car(car)


def show_cars() -> list[dict]:
    car_list = get_cars()
    return sort_cars(car_list)


def remove_car(identifier: int) -> bool:
    return try_delete_car(identifier)