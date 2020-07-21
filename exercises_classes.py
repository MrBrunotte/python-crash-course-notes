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
