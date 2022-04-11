from person import Person
import time


class Seller(Person):
    def __init__(self, name, surname, city):
        super(Seller, self).__init__(name, surname, city)
        self.car_park = {}
        self.__money = 0
        self.sold_cars = []

    def __add_discount(self, car_name):
        percent = int(input("Select discount rate.. "))
        price = self.car_park[car_name]
        discounted_price = price - (price / 100 * percent)
        self.car_park[car_name] = discounted_price
        return discounted_price

    def sell(self, car_name):
        self._check_discount(car_name=car_name)
        price = self.car_park[car_name]
        self.__change_money(price=price)
        self.add_sold_car(car_name=car_name, price=price)
        del self.car_park[car_name]
        print(f"Seller {self.name} {self.surname} earn {price} and has {self.__money}$  in wallet after "
              f"selling {car_name}")

    def __change_money(self, price):
        self.__money += price
        return self.__money

    def return_car(self, car_name):
        print(f" Before return money was {self.__money}")
        try:
            for i in range(len(self.sold_cars)):
                if self.sold_cars[i][0] == f"{car_name}":
                    self.__money -= self.sold_cars[i][1]
                    self.car_park[car_name] = self.sold_cars[i][1]
                    self.sold_cars.remove(self.sold_cars[i])
                    print(f" After return money is {self.__money}, in car park there are: {self.car_park}, "
                          f"sold cars: {self.__get_available_cars()}")
                    break
                raise AttributeError
        except AttributeError as error:
            print(error, "Such car wasn't sold, so you can't return it")

    def getavialable_cars(self):
        return self.__get_available_cars()

    def __get_available_cars(self):
        if isinstance(self, Seller) and len(self.car_park) > 0:
            car_park = self.car_park
            return car_park
        else:
            return "Car park is empty"

    def _check_discount(self, car_name):
        print("Do you want to make discount for Buyer: y or n")
        answer = input("Make your choice:  ").lower()
        if answer == "y":
            return self.__add_discount(car_name=car_name)
        elif answer == "n":
            return "Sorry, for that car isn't discount"

    def add_sold_car(self, car_name, price):
        named_tuple = time.localtime()
        time_string = time.strftime("%m/%d/%Y", named_tuple)
        self.sold_cars.append([car_name, price, self.name, self.surname, self.city, time_string])

    def __repr__(self):
        initials = self.name
        return initials


ashot = Seller("Ashot", "Ashotyan", "Erevan")
ashot.car_park['BMW'] = 3000
ashot.car_park["Nissan"] = 4000
ashot.car_park["Mercedes"] = 4000
# ashot.sell("Nissan")
# ashot.sell("BMW")
# print(ashot.__get_available_cars)
# print(ashot.sold_cars, ashot.sold_cars)
# ashot.return_car('Nissan')
# ashot._check_discount("Nissan")
