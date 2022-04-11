from seller import Seller
from seller import ashot


class CarMarket:
    def __init__(self):
        self.cars = {}

    def add_car(self, seller_name):
        if isinstance(seller_name, Seller):
            self.cars[seller_name] = seller_name._Seller__get_available_cars()
            # return self.cars

car_market = CarMarket()
print(car_market.add_car(ashot))
print(car_market.cars)
