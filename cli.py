from car import Car
from exceptions import IdValidationError
from car_actions import add_car, show_cars, remove_car
from dataclasses import fields
from enum import Enum

def run() -> None:
    while True:
        show_menu()
        user_input = input("Choose action: ")

        if user_input == "0":
            print("\nGoodbye!\n")
            return

        handle_action(user_input)


def handle_action(user_input: str) -> None:
    match user_input:
        case "1":
            add_car_cli()
        case "2":
            remove_car_cli()
        case "3":
            show_cars_cli()
        case _:
            print("Wrong input")


def generate_car() -> Car:
    car_data = {}

    for field in fields(Car):
        if not field.init:
            continue

        while True:
            if issubclass(field.type, Enum):
                print_available_enum_fields(field.type)

            try:
                car_data[field.name] = field.type(input(f"{field.name.capitalize()}: "))
                print()
                break
            except ValueError:
                print("Incorrect value!\n")

    return Car(**car_data)


def print_available_enum_fields(field_type: type[Enum]) -> None:
    print("Fields:")
    for option in field_type:
        print(f"- {option}")
    print()


def remove_car_cli() -> None:
    print_header("REMOVE CAR")

    for car in show_cars():
        print(car)

    while True:
        try:
            user_input = int(input("\nPick ID of the car you want to remove: "))

            if remove_car(user_input):
                break

            raise IdValidationError("ID isn't valid!")
        except ValueError:
            print("Incorrect value!")
        except IdValidationError as e:
            print(e)


def add_car_cli() -> None:
    print_header("ADD CAR")

    car = generate_car()
    add_car(car)

    print(f"\nAdded {car.brand} {car.model}!")


def show_cars_cli() -> None:
    print_header("CARS")

    for car in show_cars():
        for key, value in car.items():
            if key == "identifier":
                print(f"- CAR ID: {value}")
            else:
                print(f"{key}: {value}")
        print()


def show_menu() -> None:
    print_header("WHEEL HUNTER")

    print("""1. Add a car
2. Remove a car
3. Show all cars
0. Exit
""")


def print_header(title: str) -> None:
    print(f"""
====================
{title:^20}
====================
""")