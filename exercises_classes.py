'''
Making an object from a class is called INSTANTIATION
You work with INSTANCES of a class
'''

# 9.1 - Restaurant
from random import randint, choice
from module.user import User
from classes.my_restaurant import Restaurant
from restaurant import Restaurant
excercise = "9.1 - Restaurant"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """ INITIALIZE the restaurant """
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        """ Display a summary of the restaurant """
        msg = f"The name of this restaurant is {self.name} and it serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """ Dispaly a message saying that the restaurant is open """
        msg = f"{self.name} is now open!"
        print(f"\n{msg}")


# make an INSTANCE of the class Restaurant called restaurant
restaurant = Restaurant('burger king', 'hamburger')
print(restaurant.name)
print(restaurant.cuisine_type)

# call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9.2 - Three Restaurants
excercise = "9.2 - Three Restaurants"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

burger_king = Restaurant('burger king', 'hamburger')
burger_king.describe_restaurant()

italiano = Restaurant('italiano', 'italian')
italiano.describe_restaurant()

melanders = Restaurant('melanders', 'fish')
melanders.describe_restaurant()

# 9.3 - Users
excercise = "9.3 - Users"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class User:
    """ A class representing users """

    def __init__(self, first_name, last_name, age, gender, location):
        """INITIALIZE user class"""
        self.first_name = first_name.upper()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.title()
        self.location = location.title()

    def describe_user(self):
        """ A method that describes the user """
        print(f"This is a description of the user {self.first_name}:\n")
        user = f"\t- {self.first_name} {self.last_name}\n\t- {self.age}\n\t- {self.location}"
        print(user)

    def greet_user(self):
        """A method that greets the user """
        print(f"\nHello {self.first_name} {self.last_name}!\n")


stefan = User('stefan', 'brunotte', 48, 'male', 'stockholm')
rebecca = User('rebecca', 'weiss', 48, 'female', 'stockholm')

stefan.greet_user()
stefan.describe_user()
rebecca.greet_user()
rebecca.describe_user()

# 9.4 - Number Served
excercise = "9.4 - Number Served"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """ INITIALIZE the restaurant """
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        # 1 Add attribute: number_served = 0
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"The name of this restaurant is {self.name} and it serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Dispaly a message saying that the restaurant is open"""
        msg = f"{self.name} is now open!"
        print(f"{msg}")
    # 4a add method calles set_number_served

    def set_number_served(self, number_served):
        """Lets me set the number of served customers"""
        self.number_served = number_served
    # 5a Add a method called increment_number_served

    def increment_number_served(self, number_served):
        """increments the number of served customers"""
        self.number_served += number_served


# 2 make an INSTANCE called restaurant
restaurant = Restaurant('burger king', 'hamburger')
restaurant.describe_restaurant()

# 3 Print
print(f"\nNumber served: {restaurant.number_served}")
# 4b
restaurant.number_served = 430
print(f"\nNumber served: {restaurant.number_served}")
# 4c
restaurant.set_number_served(1257)
print(f"\nNumber served: {restaurant.number_served}")
# 5b
restaurant.increment_number_served(239)
print(f"\nNumber served: {restaurant.number_served}")

# 9.4 - Login Attempt
excercise = "9.4 - Login Attempt"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class User:
    """ A class representing users """

    def __init__(self, first_name, last_name, age, gender, location):
        """INITIALIZE user class"""
        self.first_name = first_name.upper()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.title()
        self.location = location.title()
        # 1 add ny attribute
        self.login_attempts = 0

    def describe_user(self):
        """ A method that describes the user """
        print(f"This is a description of the user {self.first_name}:\n")
        user = f"\t- {self.first_name} {self.last_name}\n\t- {self.age}\n\t- {self.location}"
        print(user)

    def greet_user(self):
        """A method that greets the user """
        print(f"\nHello {self.first_name} {self.last_name}!\n")

    # 2 Write a method
    def increment_login_attempts(self):
        """A method that increments the value login_attempts by 1"""
        self.login_attempts += 1

    # 3 Write a method that resets the login attempts
    def reset_login_attempts(self):
        self.login_attempts = 0


# 4 Make an instance of the User class
stefan = User('stefan', 'brunotte', 48, 'male', 'stockholm')

# 5 Call the method increment_login_attempts
print("\nMaking 3 login attempts...")
stefan.increment_login_attempts()
stefan.increment_login_attempts()
stefan.increment_login_attempts()
print(f"  Login attempts: {stefan.login_attempts}")
# 6 Reset the login attempts
print("Resetting login attempts...")
stefan.reset_login_attempts()
print(f"  Login attempts: {stefan.login_attempts}")


# 9.6 - Ice Cream Stand
excercise = "9.6 - Ice Cream Stand"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# add the Restaurant class again! PARENT class


class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, name, cuisine_type):
        """ INITIALIZE the restaurant """
        self.name = name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"The name of this restaurant is {self.name} and it serves {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Dispaly a message saying that the restaurant is open"""
        msg = f"{self.name} is now open!"
        print(f"{msg}")

    def set_number_served(self, number_served):
        """Lets me set the number of served customers"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """increments the number of served customers"""
        self.number_served += number_served

# 1 Create the child class IceCreamStand(parent_class_name)


class IceCreamStand(Restaurant):
    """Represent an ice cream stand."""

    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand."""
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()


# 9.7 - Admin
excercise = "9.7 - Admin"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class User:
    """ A class representing users """

    def __init__(self, first_name, last_name, age, gender, location):
        """INITIALIZE user class"""
        self.first_name = first_name.upper()
        self.last_name = last_name.title()
        self.age = age
        self.gender = gender.title()
        self.location = location.title()

    def describe_user(self):
        """ A method that describes the user """
        print(f"This is a description of the user {self.first_name}:\n")
        user = f"\t- {self.first_name} {self.last_name}\n\t- {self.age}\n\t- {self.location}"
        print(user)

    def greet_user(self):
        """A method that greets the user """
        print(f"\nHello {self.first_name} {self.last_name}!\n")

# the Admin class inherites from the User class


class Admin(User):
    """Inherits from the User class"""

    def __init__(self, first_name, last_name, age, gender, location):
        """Initialises the Admin class with all attributes from parent class"""
        super().__init__(first_name, last_name, age, gender, location)
        # add an empty attribure called privilges that can store a list!
        self.privileges = []

    def show_privileges(self):
        """A method that shows the admin privileges"""
        print("\nAs an Admin you will have these privileges:\n")
        for privilige in self.privileges:
            print(f"- {privilige.title()}")


# Create an instance of Admin
stefan = Admin('stefan', 'brunotte', 48, 'male', 'stockholm')
stefan.describe_user()

# Store the privileges is a list that will go into the attribute privileges.
stefan.privileges = [
    'can add post',
    'can delete post',
    'can reset passwords',
]

# call the method
stefan.show_privileges()


# 9.8 - Privileges
excercise = "9.8 - Privileges"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


class Admin(User):
    """A user with administrative privileges."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the admin."""
        super().__init__(first_name, last_name, username, email, location)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges():
    """A class to store an admin's privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")


eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric.privileges.show_privileges()

print("\nAdding privileges...")
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()


# 9.9 - Battery Upgrade
excercise = "9.9 - Battery Upgrade"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


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

    def upgrade_battery(self):
        """Upgrade the battery if possible."""
        if self.battery_size == 75:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")


# define the child class
class ElectricCar(Car):
    """Represent aspects of a car, specfic to electric vehicles"""

    def __init__(self, make, model, year):
        """ Initialize attributes of the paret class .The super() allows you to call method from the parent!"""
        super().__init__(make, model, year)
        # Initialize attributes specifit to the child class
        self.battery = Battery()


print("Make an electric car, and check the range:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


# 9.10 - Imported Restaurant
excercise = "9.10 - Imported Restaurant"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# Imported classes are always at the top of the file!!
# from restaurant import Restaurant
print("\nfrom restaurant import Restaurant:")
channel_club = Restaurant('the channel club', 'steak and seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()

# Imported classes are always at the top of the file!!
# from classes.my_restaurant import Restaurant
print("\nfrom classes.my_restaurant import Restaurant:")
channel_club = Restaurant('seefood mania', 'seafood')
channel_club.describe_restaurant()
channel_club.open_restaurant()


# 9.11 - Import Admin
excercise = "9.11 - Import Admin"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# from module.user import User
eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()

eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
]
eric.privileges.privileges = eric_privileges

print(f"\nThe admin {eric.username} has these privileges: ")
eric.privileges.show_privileges()

# 9.12 - Multiple Modules
excercise = "9.12 - Multiple Modules"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# 9.13 - Dice
excercise = "9.13 - Dice"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# from random import randint
x = randint(1, 6)


class Die():
    """ Method that rolls a dice and displays a random side from 1-6 """

    def __init__(self, sides=6):
        """Initialize the die"""
        self.sides = sides

    def roll_die(self):
        """method that returns a random number between 1 and the number of sides"""
        return randint(1, self.sides)


print("Import: from random import randint\n")
print("Steps taken to for this exercise:")
print("\n\t1. Make an instance of the Die class")
print("\t2. Make an empty list called results to store the die-rolls")
print("\t3. for loop that loops through a range of 10 rolls")
print("\t3.1 call the roll_die method to the d6 instance and store each roll in a variable called result")
print("\t3.2 append each roll from the variable result and put it in results")
print("\t4. print a message")
print("\t4. print the random rolls from the variable results\n")

# make a 6-sided die, and show the results of 10 rolls.
# Maka an instance of the class
d6 = Die()
results = []

for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die")
print(results)

d10 = Die(sides=10)
results = []

for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die")
print(results)


d20 = Die(sides=20)

results = []

for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die")
print(results)


# 9.14 - Lottery
excercise = "9.14 - Lottery"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


possibilities = [1, 2, 'b']

winning_ticket = []
my_ticket = []

print("Let's see my ticket...")
while len(my_ticket) < 2:
    pulled_item = choice(possibilities)

    if pulled_item not in my_ticket:
        print(f"  I pulled a \t{pulled_item}!")
        my_ticket.append(pulled_item)

print("\nLet's see what the winning ticket is...")

while len(winning_ticket) < 2:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"  We pulled a \t{pulled_item}!")
        winning_ticket.append(pulled_item)

if my_ticket == winning_ticket:
    print(
        f"\nFantastic!! You won! \nmy ticket: {my_ticket} = winning ticket {winning_ticket}")
else:
    print(
        f"\nSorry, your tickets didn't match!\nmy ticket: {my_ticket} = winning ticket {winning_ticket}")

# 9.14 - Lottery Analysis
excercise = "9.14 - Lottery Analysis"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def get_winning_ticket(possibilities):
    """Return a winning ticket from a set of possibilities"""
    winning_ticket = []

    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def check_ticket(played_ticket, winning_ticket):
    """Check all elements in the played ticket. If any or not in the winning ticket, return False"""

    for element in played_ticket:
        if element not in winning_ticket:
            return False
    # if element in winning_ticket
    return True


def make_random_ticket(possibilities):
    """Return a random ticket from a set of possibilties"""
    ticket = []

    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# call method
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# max tries
max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {winning_ticket}")
