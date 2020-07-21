"""
At line 13 we difine the class called Dog. All classes in Python are capitalized!

At line 16 we define the __init__() METHOD.
The init method runs automatically when we create a new INSTANCE based on the Dog class.

At line 18, 19 the variables have the prefix self. Any variable prefixed with self is 
available to every method in the class, and we'll also be able to access these variables 
through any instance create from the Dog class.
Variables that are accessible through instances like this (self.) are called ATTRIBUTES.
"""


class Dog:
    """ A simple attempt to model a dog """

    def __init__(self, name, age):
        '''INITIALIZE name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self):
        '''Simulate a dog rolling over in response to a command'''
        print(f"{self.name.title()} rolled over!")


# MAKING AN INSTANCE FROM A CLASS
    """
    the class Dog is a set of instructions that tells Python how to make individual INSTANCES representing specific dogs
    my_dog is the INSTANCE
    """


my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)

print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print("\n")

print(f"Your dog's name is {your_dog.name.title()}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
print("\n")
# Accessing attributes (name, age in the class Dog)
# my_dog.name
