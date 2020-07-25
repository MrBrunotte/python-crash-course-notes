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

# define a parent class for battery attirbutes


class Battery():
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")


# define the child class
class ElectricCar(Car):
    """Represent aspects of a car, specfic to electric vehicles"""

    def __init__(self, make, model, year):
        """ Initialize attributes of the paret class .The super() allows you to call method from the parent!"""
        super().__init__(make, model, year)
        # Initialize attributes specifit to the child class
        self.battery = Battery()


# make an instance of the class ElectricCar
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())

# Call the method describe_battery, no print statement since i have that in the function!
# Cannot call this method any more since i made a new class called Battery and moved the function there!
# my_tesla.describe_battery()

# call the method from the class Battery
my_tesla.battery.describe_battery()
# call the get_range function through the car's battery attribute
my_tesla.battery.get_range()
