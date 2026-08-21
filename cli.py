from car import Car
from car_actions import add_car, show_cars
from dataclasses import fields

def run():
    while True:
        show_menu()
        user_input = input("Choose action: ")

        if user_input == "0":
            print("\nGoodbye!\n")
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
    print_header("ADD CAR")

    car = generate_car()
    add_car(car)

    print(f"\nAdded {car.brand} {car.model}!")


def generate_car() -> Car:
    car_data = {}

    for field in fields(Car):
        if not field.init:
            continue
        
        car_data[field.name] = field.type(input(f"{field.name.capitalize()}: "))
    return Car(**car_data)


def show_cars_cli():
    print_header("CARS")

    for car in show_cars():
        print(car)


def show_menu():
    print_header("WHEEL HUNTER")

    print("""1. Add a car
2. Show all cars
0. Exit
""")


def print_header(title):
    print(f"""
====================
{title:^20}
====================
""")