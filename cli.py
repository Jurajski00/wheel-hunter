from car import Car
from car_actions import add_car
import dataclasses

def run():
    while True:
        show_menu()
        user_input = input("Choose action: ")

        if user_input == "0":
            print("Goodbye!")
            return

        handle_action(user_input)


def handle_action(user_input):
    match user_input:
        case "1":
            add_car_cli()
        case "2":
            show_cars_cli()
        case _:
            print("Wrong input")


def add_car_cli():
    print("===================")
    print("      ADD CAR      ")
    print("===================")
    print()

    car = generate_car()
    add_car(car)
    print()
    print(f"Added {car.brand} {car.model}!")
    print()


def generate_car():
    car_data = {}
    for field in dataclasses.fields(Car):
        car_data[field.name] = field.type(input(f"{field.name.capitalize()}: "))
    return Car(**car_data)


def show_cars_cli():
    pass


def show_menu():
    print("====================")
    print("    WHEEL HUNTER    ")
    print("====================")
    print()
    print("1. Add a car")
    print("2. Show my cars")
    print("0. Exit")
    print()