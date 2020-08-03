# 11.1 - city, country
excercise = "11.1 - city, country"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def city_country(city, country):
    """Retrun a string like 'Santiago, Chile'."""
    return f"{city.title()} {country.title()}"


# 11.2 Population
excercise = "11.2 Population"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def city_country_population(city, country, population=''):
    """Retrun a string like 'Santiago, Chile'."""
    return f"{city.title()} {country.title()} {population}"


# 11.3 - Employee
excercise = "11.3 - Employee"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


class Employee():
    """A class the holds employees"""

    def __init__(self, first, last, salary):
        """Initialize the Employee class"""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        """a method that adds $5000 or a specific amount"""
        self.salary += amount
