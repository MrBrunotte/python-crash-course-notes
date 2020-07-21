print('\n########## A dictionary of similar objects ############')

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")
# longer print
# print(f"Sarah's favorite language is {favorite_languages['sarah'].title()}.")


print('\n########## Looping through all key:value pairs ############')
for key, value in favorite_languages.items():
	print(f"{key.title()}'s favorite language is {value.title()}")

print("\n#### Here I have replaces 'key' and 'value' with 'name' and 'language' to make it more descriptive ###")
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}")

print('\n########## Looping through all KEYS ############')
for key in favorite_languages.keys():
	print(key.title())

print("\n#### Here I have replaces 'key' with 'name' to make it more descriptive ###")
for name in favorite_languages.keys():
	print(name.title())

print("\n#### Printing out the key is the default so I don't need .keys() ###")
for name in favorite_languages:
	print(name.title())

print("\n#### message ####")
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}")
	if 'erin' not in favorite_languages.keys():
		print("\nErin, please take our poll!")

print("\n########## Looping through a dictionary's KEYS in a particular order ############")
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll")

print("\n########## Looping through a dictionary's Key in a particular order ############")

print("The following languages have been mentioned:")
for value in favorite_languages.values():
	print(value.title())

print("\n#### print same thing but more descriptive code")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

print("\n#### use a set to not print duplicate values (python two times!)")
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

print("\n########## A list in a dictionary ############")
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'heskell'],
}

#for name, languages in favorite_languages.items():
#	if name <= 1:
#		print(f"\n{name.title()}'s favorite language is:")
#	elif name >= 2:
#		print(f"\n{name.title()}'s favorite languages are:")
#	for language in languages:
#		print(f"\t{language.title()}")

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")


