from person import Person
from seller import Seller


class Buyer(Person):
    def __init__(self, name, surname, city):
        super(Buyer, self).__init__(name, surname, city)
        self.__money = 8000
        self.spent_money = 0
        self.bought_cars = {}

    def buy(self, seller_name, car_name):
        if isinstance(seller_name, Seller):
            seller_name.sell(car_name=car_name)
            self.add_bought_cars(seller_name=seller_name)
            price = seller_name.sold_cars[-1][-5]
            self.change_money(price=price)
            self.spent_money += price
            print(f"In buyer {gnord} wallet is {self.__money}")
            return self.bought_cars

    def return_car(self):
        pass

    def change_money(self, price):
        return self.__change_money(price=price)

    def __change_money(self, price):
        self.__money -= price
        return self.__money

    def add_bought_cars(self, seller_name):
        if seller_name not in self.bought_cars:
            self.bought_cars[seller_name] = []
        self.bought_cars[seller_name].append(seller_name.sold_cars[-1])

    def print_my_cars(self):
        return self.bought_cars

    def __repr__(self):
        name = self.name
        return name


gnord = Buyer('Azat', 'Stepanyan', 'Erevan')
