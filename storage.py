from dataclasses import asdict
from pathlib import Path
from json import dump, load
from car import Car


file_name = "listings.json"


def save_car(car: Car) -> None:
    json_file = load_file()
    car_list: list[dict] = json_file["cars"]

    car.identifier = json_file["next_id"]
    
    car_list.append(asdict(car))
    json_file["next_id"] += 1

    save_file(json_file)


def save_file(json_file: dict) -> None:
    with open(file_name, "w") as file:
        dump(json_file, file)


def load_file() -> dict:
    if not Path(file_name).exists():
        create_file()

    with open(file_name, "r") as file:
        return load(file)


def get_cars() -> list[dict]:
    json_file = load_file()
    return json_file["cars"]


def create_file() -> None:
    contents = {
        "next_id": 1,
        "cars": []
    }
    with open(file_name, "w") as file:
        dump(contents, file)