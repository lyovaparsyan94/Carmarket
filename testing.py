from seller import Seller
from seller import ashot

a = {'Ashot': {'BMW': 3000, 'Nissan': 4000, 'Mercedes': 4000}}


class CarMarket:
    def __init__(self):
        self.cars = {}

    def set_discount(self, seller_name, car_name):
        if bool(self.cars):
            return True
        elif not bool(self.cars):
            return False


car_market = CarMarket()

print(car_market.set_discount(ashot, "BMW"))
