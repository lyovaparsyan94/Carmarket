from seller import Seller
from seller import ashot
from buyer import gnord
from buyer import Buyer

import time


class CarMarket:
    def __init__(self):
        self.cars = {}

    def add_car(self, seller_name):
        if isinstance(seller_name, Seller):
            self.cars[f'{seller_name}'] = seller_name.get_avialable_cars()
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

    def _set_discount(self, seller_name, car_name):
        if bool(self.cars):
            if car_name in self.cars[f'{seller_name}']:
                print("Asking Seller for discount...")
                new_price = seller_name._check_discount(car_name=car_name)
                self.cars[f'{seller_name}'][car_name] = new_price
                return self.cars
        elif not bool(self.cars):
            print("Empty list")

    def get_sold_car_history(self, seller_name):
        return self._get_sold_car_history(seller_name=seller_name)

    def _get_sold_car_history(self, seller_name):
        return self._get_sold_cars_history(seller_name=seller_name)

    def _get_sold_cars_history(self, seller_name):
        if isinstance(seller_name, Seller):
            return seller_name.sold_cars

    def return_car(self, seller_name, car_name):
        return self._return_car(seller_name=seller_name, car_name=car_name)

    def _return_car(self, seller_name, car_name):
        if isinstance(seller_name, Seller):
            return seller_name.return_car(car_name=car_name)

    def get_seller_avialable_cars(self, seller_name):
        return self._get_seller_available_cars(seller_name=seller_name)

    def _get_seller_available_cars(self, seller_name):
        if isinstance(seller_name, Seller):
            return seller_name.get_avialable_cars()

    def get_car_available_discount(self, seller_name, car_name):
        if isinstance(seller_name, Seller):
            return seller_name._check_discount(car_name=car_name)


car_market = CarMarket()
# car_market.add_car(ashot)
# print(car_market.cars)
# print(gnord.buy(ashot, "Nissan"))
# print(gnord.buy(ashot, "Mercedes"))
print(gnord.buy(ashot, "BMW"))
gnord.return_car(ashot, "BMW")
print(car_market.cars)
# print(car_market.get_sold_car_history(ashot))