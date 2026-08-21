from storage import get_id, save_car, get_cars

def add_car(car):
    car.identifier = get_id()
    save_car(car)


def show_cars():
    return get_cars()