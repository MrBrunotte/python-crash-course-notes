'''
Making an object from a class is called INSTANTIATION
You work with INSTANCES of a class
'''

# 9.1 - Restaurant
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


# 9.5 - Ice Cream Stand
excercise = "9.5 - Ice Cream Stand"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")
