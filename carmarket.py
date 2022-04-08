from seller import Seller
from buyer import Buyer


class CarMarket:
    def __init__(self):
        self.cars = []

    def add_car(self, car_mark: str):
        self.cars.append(car_mark)

    def remove_car(self):
        pass

    def __set_discount(self):
        pass

    def _get_sold_car_history(self):
        pass

    def _return_car(self):
        pass

    def _get_seller_available_cars(self):
        return

    def get_car_available_discount(self):
        pass

car_market = CarMarket()
print(car_market.add_car("Opel"))
print(car_market.cars)