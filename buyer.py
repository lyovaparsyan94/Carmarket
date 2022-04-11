from person import Person
# from seller import ashot


class Buyer(Person):
    def __init__(self, name, surname, city, money):
        super(Buyer, self).__init__(name, surname, city)
        self.money = int(money)
        self.spent_money = 0
        self.bought_cars = []

    def buy(self, car_name):
        pass

    def return_car(self):
        pass

    def _change_money(self, added_money):
        result = added_money + self.money
        return result

    def add_bought_cars(self):
        pass

    def print_my_cars(self):
        pass


# Ashot = Buyer('Ashot', 'Stepanyan', 'Erevan', 5000)
#
#
# print(Ashot._change_money(5000))
