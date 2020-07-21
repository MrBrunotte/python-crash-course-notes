print('\n########## Try it yourself: 6-1 Person ############')
my_info = {
	'first_name': 'stefan',
	'last_name': 'brunotte',
	'age': 48,
	'city': 'stockholm',
}

print(f"My name is {my_info['first_name'].title()}")
print(f"My last name is {my_info['last_name'].title()}")
print(f"My age is {my_info['age']}")
print(f"I live in {my_info['city'].title()}")

print('\n########## Try it yourself: 6-2 Favorite numbers ############')
favorite_numbers = {
	'viggo': 5,
	'rebecca': 6,
	'hedda': 7,
	'isac': 8,
	'herman': 9,
}

num = favorite_numbers['viggo']
print(f"Viggo's favorite number is: {num}")
num = favorite_numbers['rebecca']
print(f"Rebecca's favorite number is: {num}")
num = favorite_numbers['hedda']
print(f"Hedda's favorite number is: {num}")
num = favorite_numbers['isac']
print(f"Isac's favorite number is: {num}")
num = favorite_numbers['herman']
print(f"Herman's favorite number is: {num}")

print('\n########## Try it yourself: 6-3 Clossary ############')
glossary = {
	'list': 'A list is a collection of items in a particular order.',
	'pop': 'The pop() method removes the last item in a list, but it lets you work with that item after removing it!',
	'sort': 'The sort() method changes the order of a list permanently',
	'sorted': 'The sorted() methos changes the list order temporarily',
	'dictionary': 'A dictionary in Python is a collection of key:value pairs',
}

meaning = 'list'
print(f"\n{meaning.upper()}:\t{glossary[meaning]}")
meaning = 'pop'
print(f"\n{meaning.upper()}:\t{glossary[meaning]}")
meaning = 'sort'
print(f"\n{meaning.upper()}:\t{glossary[meaning]}")
meaning = 'sorted'
print(f"\n{meaning.upper()}:\t{glossary[meaning]}")
meaning = 'dictionary'
print(f"\n{meaning.upper()}:\t{glossary[meaning]}")

print('\n########## Try it yourself: 6-4 Clossary 2 ############')
glossary = {
	'list': 'A list is a collection of items in a particular order.',
	'pop': 'The pop() method removes the last item in a list, but it lets you work with that item after removing it!',
	'sort': 'The sort() method changes the order of a list permanently',
	'sorted': 'The sorted() methos changes the list order temporarily',
	'dictionary': 'A dictionary in Python is a collection of key:value pairs',
}

glossary2 = {
	'list': 'A list is a collection of items in a particular order.',
	'pop': 'The pop() method removes the last item in a list, but it lets you work with that item after removing it!',
	'sort': 'The sort() method changes the order of a list permanently',
	'sorted': 'The sorted() methos changes the list order temporarily',
	'dictionary': 'A dictionary in Python is a collection of key:value pairs',
	'if elif else chain': 'is used to test more than two possible situations',
	'for loop': 'is used to loop through something to get all the elements or items',
	'for loop and keys()': 'lets you loop through all key´s in a dictionary',
	'for loop and values()': 'lets you loop trhough all the values in a dictionary',
}

print(f"#### Printing the dictionary: GLOSSARY")
for key, value in glossary.items():
	print(f"{key.upper()}:\t{value.title()}")
print("\n#### Printing the dictionary: GLOSSARY2")
for name, description in glossary2.items():
	print(f"{name.upper()}:\t{description.title()}")

print('\n########## Try it yourself: 6-5 Rivers ############')
rivers = {
	'nile': 'egypt', 
	'mississippi': 'usa', 
	'amazon river': 'south america',
}
print("#### Usa for loop to print the message 'The river runs through country'")
for river_name,country in rivers.items():
	print(f"The {river_name.title()} runs through {country.title()}!")
print("\n#### Usa a for loop to print the name of each river (keys item)")
for river_name in rivers.keys():
	print(river_name.title())
print("\n#### Usa a for loop to print the name of each country (values item)")
for country in rivers.values():
	print(country.title())

print('\n########## Try it yourself: 6-6 Polling ############')
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
print("\n#### Printing the names and languages:")
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")
print("\n#### make a new list with new people and people from the previous list")

coders = ['jen', 'peter', 'sarah', 'stefan', 'rebecca', 'viggo', 'isac', 'edward']

for coder in coders:
	if coder in favorite_languages.keys():
		print(f"Thank you for doing the poll {coder.upper()}!")
	else:
		print(f"{coder.title()}, what's your favorite programming language?")

print('\n########## Try it yourself: 6-7 People ############')

print("1) make empty list to store people in")
people = []

print("2) define some people and add them to the list 'people.append(person)'")
person = {
	'first_name': 'stefan',
	'last_name': 'brunotte',
	'age': 48,
	'city': 'stockholm',
}
people.append(person)

person = {
	'first_name': 'rebecca',
	'last_name': 'weiss',
	'age': 48,
	'city': 'stockholm',
}
people.append(person)

person = {
	'first_name': 'viggo',
	'last_name': 'brunotte',
	'age': 1.7,
	'city': 'stockholm',
}
people.append(person)

print(people)

print("3) display all of the information in the dictonary\n")
for person in people:
	name = f"{person['first_name'].title()} {person['last_name'].title()}"
	age = person['age']
	city = person['city'].title()

	print(f"{name}, of {city}, is {age} years old!")

print('\n########## Try it yourself: 6-8 Pets ############')

pets = []

pet = {
	'owner': 'rebecca',
	'animal': 'dog',
	'name': 'hedda',
}
pets.append(pet)
pet = {
	'owner' : 'stefan',
	'animal': 'shark',
	'name': 'sharky shark',
}
pets.append(pet)
pet = {
	'owner': 'viggo',
	'animal': 'mouse',
	'name': 'mickey',
}
pets.append(pet)
pet = {
	'owner': 'mamma',
	'animal': 'lion',
	'name': 'leo the lion',
}
pets.append(pet)

print(pets)

for pet in pets:
	print(f"Here is what I know about {pet['name']}:")
	for key, value in pet.items():
		print(f"\t{key.title()}: {value.title()}")

print('\n########## Try it yourself: 6-9 Favorite places ############')
favorite_places = {
	'stefan': ['antibes', 'hawaii', 'lake como'],
	'rebecca': ['hawaii', 'santa monica'],
	'viggo': ['bahamas', 'honolulu', 'copenhagen']
}

for name, places in favorite_places.items():
	print(f"\n{name.title()} likes the follwing places:")
	for place in places:
		print(f"- {place.title()}")

print('\n########## Try it yourself: 6-10 Favorite numbers ############')

favorite_numbers = {
	'viggo': [5,9,25,53],
	'rebecca': [6,9,3,7],
	'hedda': [7,1,5,2,3],
	'isac': [8,7,4,0,3,],
	'herman': [9,100,562,5415,8784512],
}
for name, numbers in favorite_numbers.items():
	print(f"\n{name.title()}'s favorite numbers are:")
	for num in numbers:
		print(f"\t{num}")

print('\n########## Try it yourself: 6-11 Cities ############')

cities = {
	'stockholm': {
		'country': 'sweden',
		'population': 2_000_000,
		'airport': 'arlanda'
	},
	'new york': {
		'country': 'usa',
		'population': 12_000_000,
		'airport': 'jfk',
	},
	'antibes': {
		'country': 'france',
		'population': 800_000,
		'airport': 'nice',
	},
}

for city, city_info in cities.items():
	country = city_info['country'].title()
	population = city_info['population']
	airport = city_info['airport'].title()

	print(f"\n{city.title()} is in {country}.")
	print(f"\tIt has a population of about {population}.")
	print(f"\tThe name of the airport is {airport}.")

print('\n########## Try it yourself: 6-12 Extensions ############')
