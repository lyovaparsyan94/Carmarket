import time


class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city


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
            # print(f"In buyer {gnord} was withdrawn {price}, in wallet is {self.__money}")
            # car_market.cars[]
            return self.bought_cars

    def return_car(self, seller_name, car_name):
        print(f'Returning...buyers money - {self.__money}, spent money - {self.spent_money}, bought cars - {self.bought_cars}')
        print(f"Searching in list related with {seller_name}: ", self.bought_cars[seller_name])
        sellers_purchases = self.bought_cars[seller_name]
        for i in sellers_purchases:
            if i[0] ==car_name and i[2] == f'{seller_name}':
                print(f"Two-factor verification by seller's name '{seller_name}' and car brand '{car_name}'")
                self.__money += i[1]
                self.spent_money -= i[1]
                sellers_purchases.remove(i)
        car_market.return_car(seller_name=seller_name, car_name=car_name)
        if isinstance(seller_name, Seller):
            seller_name.return_car(car_name=car_name)
        print(f'buyers money - {self.__money}, spent money - {self.spent_money}, bought cars - {self.bought_cars}')


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


class Seller(Person):
    def __init__(self, name, surname, city):
        super(Seller, self).__init__(name, surname, city)
        self.car_park = {}
        self.__money = 0
        self.sold_cars = []

    def __add_discount(self, car_name):
        percent = 10
        price = self.car_park[car_name]
        discounted_price = price - (price / 100 * percent)
        self.car_park[car_name] = discounted_price
        # print(f"You have received discount {percent}%, cost of this car will be {discounted_price}$ instead of {price}$")
        return discounted_price

    def sell(self, car_name):
        self._check_discount(car_name=car_name)
        price = self.car_park[car_name]
        self.__change_money(price=price)
        self.add_sold_car(car_name=car_name, price=price)
        del self.car_park[car_name]
        # if isinstance(car_market, ):
        #     car_market.add_car(seller_name=self.name)
        # print(f"Seller {self.name} {self.surname} earn {price} and has {self.__money}$  in wallet after "
        #       f"selling {car_name}")

    def __change_money(self, price):
        self.__money += price
        return self.__money

    def return_car(self, car_name):
        # print(f" Before return money was {self.__money}")
        try:
            for i in range(len(self.sold_cars)):
                print(f"Checking {self.name}'s wallet ...")
                if self.sold_cars[i][0] == f"{car_name}" and self.__money >= self.sold_cars[i][1]:
                    print(f" {self.sold_cars[i][1]} $ will be withdrawn from the wallet.")
                    self.__money -= self.sold_cars[i][1]
                    self.car_park[car_name] = self.sold_cars[i][1]
                    self.sold_cars.remove(self.sold_cars[i])
                    print(f" After returning seller's money is {self.__money}, in car park there are: {self.car_park}, "
                          f"sold cars: {self.sold_cars}")
                    return "Successful"
                raise AttributeError
        except AttributeError as error:
            return error, "Such car wasn't sold, so you can't return it"

    def get_avialable_cars(self):
        return self.__get_available_cars()

    def __get_available_cars(self):
        if isinstance(self, Seller) and len(self.car_park) > 0:
            car_park = self.car_park
            return car_park
        else:
            return "Car park is empty"

    def _check_discount(self, car_name):
        # print("Do you want to make discount 10% for Buyer: y or n")
        # answer = input("Make your choice:  ").lower()
        answer = "y"
        if answer == "y":
            return self.__add_discount(car_name=car_name)
        elif answer == "n":
            return "Sorry, for that car there is not discount"

    def add_sold_car(self, car_name, price):
        named_tuple = time.localtime()
        time_string = time.strftime("%m/%d/%Y", named_tuple)
        self.sold_cars.append([car_name, price, self.name, self.surname, self.city, time_string])

    def __repr__(self):
        initials = self.name
        return initials


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
gnord = Buyer('Azat', 'Stepanyan', 'Erevan')
ashot = Seller("Ashot", "Ashotyan", "Erevan")
ashot.car_park['BMW'] = 3000
# ashot.car_park["Nissan"] = 4000
# ashot.car_park["Mercedes"] = 4000
print(gnord.buy(ashot, "BMW"))
gnord.return_car(ashot, "BMW")
# print(car_market.cars)