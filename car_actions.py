from storage import *
from car import *
import dataclasses

def add_car(car):
    car.identifier = get_id()
    save_car(car)


def show_cars():
    return get_cars()