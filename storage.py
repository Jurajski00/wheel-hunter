from dataclasses import asdict
from pathlib import Path
from json import dump, load
from car import Car

FILE_NAME = "listings.json"

def save_car(car: Car) -> None:
    json_file = load_file()
    car_list: list[dict] = json_file["cars"]
    
    car_list.append(asdict(car))
    json_file["next_id"] += 1

    save_file(json_file)


def try_delete_car(identifier: int) -> bool:
    json_file = load_file()
    car_list: list[dict] = json_file["cars"]

    for car in car_list:
        if car["identifier"] == identifier:
            car_list.remove(car)
            save_file(json_file)
            return True

    return False


def save_file(json_file: dict) -> None:
    with open(FILE_NAME, "w") as file:
        dump(json_file, file)


def load_file() -> dict:
    if not Path(FILE_NAME).exists():
        create_file()

    with open(FILE_NAME, "r") as file:
        return load(file)


def create_file() -> None:
    contents = {
        "next_id": 1,
        "cars": []
    }
    with open(FILE_NAME, "w") as file:
        dump(contents, file)


def get_cars() -> list[dict]:
    json_file = load_file()
    return json_file["cars"]


def get_next_id() -> int:
    json_file = load_file()
    return json_file["next_id"]