from car import *
from car_actions import *
import dataclasses

def run():
    while True:
        show_menu()
        user_input = input("Choose action: ")

        if user_input == "0":
            print("Goodbye!")
            print()
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
            print()


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


def generate_car() -> Car:
    car_data = {}

    for field in dataclasses.fields(Car):
        if not field.init:
            continue

        car_data[field.name] = field.type(input(f"{field.name.capitalize()}: "))
    return Car(**car_data)


def show_cars_cli():
    print("==================")
    print("       CARS       ")
    print("==================")
    print()
    for car in show_cars():
        print(car)
    print()


def show_menu():
    print("====================")
    print("    WHEEL HUNTER    ")
    print("====================")
    print()
    print("1. Add a car")
    print("2. Show my cars")
    print("0. Exit")
    print()