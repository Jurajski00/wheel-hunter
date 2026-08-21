from dataclasses import asdict
from pathlib import Path
from json import dump, load

file_name = "listings.json"

def save_car(car):
    json_file = load_cars()
    car_list = json_file["cars"]

    car_list.append(asdict(car))
    json_file["cars"] = car_list
    json_file["next_id"] += 1

    with open(file_name, "w") as file:
        dump(json_file, file)


def load_cars():
    if not Path(file_name).exists():
        create_file()

    with open(file_name, "r") as file:
        return load(file)


def get_id():
    json_file = load_cars()
    return json_file["next_id"]

def get_cars():
    json_file = load_cars()

    return json_file["cars"]


def create_file():
    with open(file_name, "w") as file:
        contents = {
            "next_id": 1,
            "cars": []
        }
        
        dump(contents, file)