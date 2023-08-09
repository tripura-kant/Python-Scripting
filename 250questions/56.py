# Setting a Default vaues for an Attributes


# Working with classes and instances

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 30

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can rollback an odometer")


my_new_car = Car('audi', 'a2', 2023)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(50)
my_new_car.read_odometer()
