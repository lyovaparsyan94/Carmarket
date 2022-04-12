from seller import Seller
from seller import ashot


class CarMarket:
    def __init__(self):
        self.cars = {'Ashot': {'BMW': 3000, 'Nissan': 4000, 'Mercedes': 4000}}

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



car_market = CarMarket()
print(car_market.set_discount(ashot, "BMW"))
