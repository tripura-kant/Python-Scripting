# Working with classes and instances

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a2', 2023)
print(my_new_car.get_descriptive_name())
