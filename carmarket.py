from seller import Seller
from seller import ashot
from buyer import Buyer
import time


class CarMarket:
    def __init__(self):
        self.cars = []

    def add_car(self, seller_name):
        if isinstance(seller_name, Seller):
            self.cars.append({seller_name.name: seller_name.car_park})
            return self.cars
        else:
            return "No permission"

    def remove_car(self, car_name):
        if len(self.cars) > 0:
            self.cars.remove(car_name)
            return self.cars
        else:
            return "Impossible remove car from empty list"

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
# print(car_market.add_car(ashot))
car_market.remove_car()