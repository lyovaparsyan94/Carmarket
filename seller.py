from person import Person


class Seller(Person):
    def __init__(self, name, surname, city, money):
        super(Seller, self).__init__(name, surname, city)
        self.car_park = []
        self.__money = money
        self.sold_cars = []

    def sell(self, car_mark):
        self.car_park.remove(car_mark)
        print("Car was sold")
        self.sold_cars.append(car_mark)
        Seller.__change_money()
        return self.car_park

    def __change_money(self, added_money):
        result = added_money + self.__money
        return result

    def return_car(self):
        pass

    def __get_available_cars(self):
        pass

    def __check_discount(self):
        pass

    def add_sold_car(self):
        pass


a = Seller("Ashot", "Ashotyan", "Erevan", 1000)

# a.car_park.append("Opel")
# print(a.car_park)
