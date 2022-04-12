from seller import Seller
from seller import ashot

a = {'Ashot': {'BMW': 3000, 'Nissan': 4000, 'Mercedes': 4000}}


class CarMarket:
    def __init__(self):
        self.cars = {}

    def get_sold_car_history(self, seller_name):
        return self._get_sold_car_history

    def _get_sold_car_history(self, seller_name):
        if isinstance(seller_name, Seller):
            return seller_name.sold_cars


car_market = CarMarket()

# print(car_market._get_sold_car_history(ashot))
