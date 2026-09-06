from storage import save_car, get_cars, try_delete_car, get_next_id
from scoring import get_score 
from car import Car

def add_car(car: Car) -> None:
    car.identifier = get_next_id()
    car.score = get_score(car)
    save_car(car)


def remove_car(identifier: int) -> bool:
    return try_delete_car(identifier)


def show_cars() -> list[dict]:
    car_list = get_cars()
    return sort_car_list(car_list)


def sort_car_list(car_list: list[dict]) -> list[dict]:
    car_list.sort(reverse=True, key=car_sort_key)
    return car_list


def car_sort_key(car: dict) -> int:
    return car["score"]