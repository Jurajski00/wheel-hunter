from dataclasses import asdict
import json

def save_car(car):
    with open("listings.json", "a") as file:
        json.dump(asdict(car), file)