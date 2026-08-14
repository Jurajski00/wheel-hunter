from car import Car
from car_actions import add_car

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

    car_data = {
        "brand": input("Brand: "),
        "model": input("Model: "),
        "year": int(input("Year: ")),
        "price": int(input("Price: ")),
        "mileage": int(input("Mileage: ")),
        "url": input("Url: "),
    }

    car = Car(**car_data)
    add_car(car)
    print(f"Added {car.brand} {car.model}!")


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