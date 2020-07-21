class Car:
    """ A simple attempt to represent a car """

    def __init__(self, make, model, year):
        """ Initialize attributes to describe car """
        self.make = make.upper()
        self.model = model.title()
        self.year = year
        self.odometer_reading = 15

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """ Print a statement showing the car's mileage """
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """ A method that updates the odomenter with the given value
            Reject the change if it attempts to roll the odometer back 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading """
        self.odometer_reading += miles


my_new_car = Car('Audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
# modifying an Attributes value directly!
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

# modifying an attributes with a method
my_new_car.update_odometer(45)
my_new_car.read_odometer()
print("\n")
my_new_car.update_odometer(10)
my_new_car.read_odometer()
print("\n")

# Incrementing an Attributes value through a method
my_used_car = Car('suburu', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
