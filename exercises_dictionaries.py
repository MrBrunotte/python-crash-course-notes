# 6.1 - Person

import random
excercise = "6.1 - Person"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

person = {
    'first_name': 'stefan',
    'last_name': 'brunotte',
    'age': 48,
    'city': 'stockholm'
}
print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

# 6.2 - Favorite Numbers
excercise = "6.2 - Favorite Numbers"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

favorite_numbers = {
    'stefan': 5,
    'rebecca': 6,
    'viggo': 7,
    'hedda': 8,
    'isac': 9,
    'herman': 10,
}
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}")

print("\n")
for name in favorite_numbers.keys():
    print(f"{name.title()}")

print("\n")
for number in favorite_numbers.values():
    print(f"{number}")

# number = input('\nWhat is your favourit number? ')
# print(number)

# 6.3 - Glossary
excercise = "6.3 - Glossary"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

glossary = {
    'pop()': 'Removes the last item in a list. It can be stored in a variable',
    'print()': 'The print() function prints a message and a variable',
    'get()': 'The get() method lets you set a default value to be displayed if the requested key does not exist',
    'del': 'You use del to remove a key:value pair',
    'dictionary': 'uses key:value pairs'
}

for key, value in glossary.items():
    print(f"The meaning of the word: '{key}' in Pyton is:\n\t{value}")

# 6.4 - Glossary 2
excercise = "6.4 - Glossary 2"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

print("I already did this in the first Glossary exercise!")

# 6.5 - Rivers
excercise = "6.5 - Rivers"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

rivers = {
    'nile': 'egypt',
    'rehn': 'germany',
    'mississippi': 'usa',
}

for river, country in rivers.items():
    if country == 'usa':
        print(f"The river {river.title()} runs through the {country.upper()}")
    else:
        print(f"The river {river.title()} runs through {country.title()}")

print("\n")
for river in rivers.keys():
    print(river.title())

print("\n")
for country in rivers.values():
    if country == 'usa':
        print(country.upper())
    else:
        print(country.title())

# 6.6 - Polling
excercise = "6.6 - Polling"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite coding language is: {language.upper()}")

print("\n")

not_polled_yet = ['stefan', 'rebecca', 'jen', 'sarah']

for name in not_polled_yet:
    if name in favorite_languages.keys():
        print(f"Thank you {name.title()} for already doing the poll!")
    else:
        print(f"{name.title()}, please take the poll now!")

# 6.7 - People
excercise = "6.7 - People"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# Empty list to store people in
people = []

# Define someone and append them to the variable people
person = {
    'first_name': 'stefan',
    'last_name': 'brunotte',
    'age': 48,
    'city': 'stockholm'
}
people.append(person)

person = {
    'first_name': 'rebecca',
    'last_name': 'weiss',
    'age': 48,
    'city': 'stockholm'
}
people.append(person)

person = {
    'first_name': 'viggo',
    'last_name': 'brunotte',
    'age': 1.5,
    'city': 'stockholm'
}
people.append(person)

# loop through people
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print((f"{name} is {age} years old and lives in {city.title()}"))

# 6.8 - Pets
excercise = "6.8 - Pets"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

pets = []

animal = {
    'animal_type': 'dog',
    'name': 'hedda',
    'owner_first_name': 'rebecca',
    'owner_last_name': 'weiss',
}
pets.append(animal)

animal = {
    'animal_type': 'gold-fish',
    'name': 'lola',
    'owner_first_name': 'ruth',
    'owner_last_name': 'brunotte',
}
pets.append(animal)

animal = {
    'animal_type': 'cat',
    'name': 'buster',
    'owner_first_name': 'isac',
    'owner_last_name': 'mansson',
}
pets.append(animal)

animal = {
    'animal_type': 'shark',
    'name': 'jaws',
    'owner_first_name': 'stefan',
    'owner_last_name': 'brunotte',
}
pets.append(animal)

for animal in pets:
    print(f"\nHere is what I know about {animal['name'].title()}:\n")
    for key, value in animal.items():
        print(f"\t{key.title()} - {value.upper()}")

# 6.9 - Favorite Places
excercise = "6.9 - Favorite Places"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

favorite_places = {
    'stefan': ['antibes', 'hawaii', 'the alps'],
    'rebecca': ['hawaii', 'bora bora'],
    'viggo': ['nassau'],
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name.title()}'s favorite place is:")
        for place in places:
            print(f"- {place.title()}")

    if len(places) > 1:
        print(f"{name.title()}'s favorite places are:")
        for place in places:
            print(f"- {place.title()}")

# 6.10 - Favorite Numbers
excercise = "6.10 - Favorite Numbers"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


favorite_numbers = {
    'stefan': [7, 4, 5, 9],
    'rebecca': [5, 8, 2, 9, 100, 99],
    'viggo': [3, 6, 4, 9, 2],
    'hedda': [4, 5, 7, 2, 4, 7],
    'isac': [11, 22, 2, 4, 56, 69],
    'herman': [65, 245, 2145, 1],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f" {number}")

# 6.11 - Cities
excercise = "6.11 - Cities"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

cities = {
    'new york': {
        'country': 'usa',
        'population': 12_000_000,
        'fact': 'nice place to vacation!'
    },
    'antibes': {
        'country': 'france',
        'population': 50_000,
        'fact': 'we will build a house here in the future!!'
    },
    'stockholm': {
        'country': 'sweden',
        'population': 2_000_000,
        'fact': 'where we live and capital of sweden.'
    },
}

for city, city_info in cities.items():
    country = city_info['country'].capitalize()
    population = city_info['population']
    fact = city_info['fact']
    print(country.upper())
    print(f"\tCity:\t\t {city.title()}")
    print(f"\tPopulation:\t {population}")
    print(f"\tFact:\t\t {fact.capitalize()}")
