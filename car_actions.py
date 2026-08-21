from storage import save_car, get_cars, save_file, load_file
from car import Car

def add_car(car: Car) -> None:
    save_car(car)


def show_cars() -> list[dict]:
    return get_cars()


def remove_car(id: int) -> None:
    json_file = load_file()
    car_list: list[dict] = json_file["cars"]

    for car in car_list:
        if car["identifier"] == id:
            car_list.remove(car)
            break

    save_file(json_file)