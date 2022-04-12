from seller import Seller
from seller import ashot
from buyer import Buyer
import time


class CarMarket:
    def __init__(self):
        self.cars = {}

    def add_car(self, seller_name):
        if isinstance(seller_name, Seller):
            self.cars[f'{seller_name}'] = seller_name.getavialable_cars()
            return car_market.cars
        else:
            return "No permission"

    def remove_car(self, seller_name, car_name):
        try:
            if car_name in self.cars[f'{seller_name}']:
                del self.cars[f'{seller_name}'][car_name]
                return f"{seller_name}'s {car_name}  was removed from Carmarket"
            raise KeyError
        except KeyError as e:
            print(e, "Impossible remove car from Carmarket")

    def set_discount(self, seller_name, car_name):
        if car_name in self.cars[f'{seller_name}']:
            print("Asking Seller for discount...")
            new_price = seller_name._check_discount(car_name=car_name)
            self.cars[f'{seller_name}'][car_name] = new_price
            return (self.cars)

    def _get_sold_car_history(self):
        pass

    def _return_car(self):
        pass

    def _get_seller_available_cars(self):
        return

    def get_car_available_discount(self):
        pass

car_market = CarMarket()
# # print(car_market.add_car(ashot))
# car_market.add_car(ashot)
# print(car_market.cars)