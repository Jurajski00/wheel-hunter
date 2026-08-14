from storage import *

def add_car(car):
    save_car(car)


def show_cars() -> list:
    return load_cars()