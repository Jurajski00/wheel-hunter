from dataclasses import asdict
from pathlib import Path
import json

def save_car(car):
    car_list = load_cars()

    car_list.append(asdict(car))

    with open("listings.json", "w") as file:
        json.dump(car_list, file)


def load_cars() -> list:
    if not Path("listings.json").exists():
        return []

    car_list = []

    with open("listings.json", "r") as file:
        car_list = json.load(file)

    return car_list