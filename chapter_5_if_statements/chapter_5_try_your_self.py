print("\n5-1 CONDITIONAL TEST\n")
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')

print("Is car == 'audi'? I predict False")
print(car == 'audi')

print("\n5-2 MORE CONDITIONAL TESTS")

print("\n5-3 ALIEN COLORS #1")
alien_color = 'green'
if alien_color == 'green':
	print("You got 5 points!")

alien_color = 'red'
if alien_color == 'green':
	print("You got 5 points!")


print("\n5-4 ALIEN COLORS #2")
alien_color = 'green'
if alien_color == 'green':
	print("You got 5 points!")
else: 
	print("You got 10 points")

alien_color = 'red'
if alien_color == 'green':
	print("You got 5 points!")
else: 
	print("You got 10 points")

print("\n5-5 ALIEN COLORS #3")
alien_color = 'green'
if alien_color == 'green':
	print("You got 5 points!")
elif alien_color == 'yellow': 
	print("You got 10 points")
elif alien_color == 'red':
	print("You got 15 points")

alien_color = 'yellow'
if alien_color == 'green':
	print("You got 5 points!")
elif alien_color == 'yellow': 
	print("You got 10 points")
elif alien_color == 'red':
	print("You got 15 points")

alien_color = 'red'
if alien_color == 'green':
	print("You got 5 points!")
elif alien_color == 'yellow': 
	print("You got 10 points")
elif alien_color == 'red':
	print("You got 15 points")

print("\n5-6 STAGES OF LIFE")
age = 19.99

if age < 2:
	print("You are a baby")
elif age == 2 or age < 4:
	print("You are a toddler")
elif age == 4 or age < 13:
	print("You are a kid")
elif age == 13 or age < 20:
	print("You are a teenager")
elif age == 20 or age < 65:
	print("You are an adult")
else:
	print("You are an elder")

print("\n5-7 FAVORTE FRUIT")

favorite_fruits = ['apple' ,'banana', 'mango']

if 'apple' in favorite_fruits:
	print("You really like apples!")
if 'pear' in favorite_fruits:
	print("You really like pears!")
if 'banana' in favorite_fruits:
	print("You really like bananas!")
if 'mango' in favorite_fruits:
	print("You really like mangos!")
if 'pineapple' in favorite_fruits:
	print("You really like pinapples!")

print("\n5-8 HELLO ADMIN")
names = ['admin', 'stefan', 'viggo', 'rebecca', 'herman', 'isac']

for name in names:
	if name == 'admin':
		print('Hello admin, would you like to see a status report?')
	else:
		print(f'Hello {name}! Thank you for logging in again!')

print("\n5-9 NO USER")

names = []

if names:
	for name in names:
		if name == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print(f'Hello {name}! Thank you for logging in again!')
else: 
	print("We need to find some users!")

names = ['rebecca']
if names:
	for name in names:
		if name == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print(f'Hello {name}! Thank you for logging in again!')
else: 
	print("We need to find some users")

names = ['admin']
if names:
	for name in names:
		if name == 'admin':
			print('Hello admin, would you like to see a status report?')
		else:
			print(f'Hello {name}! Thank you for logging in again!')
else: 
	print("We need to find some users")

print("\n5-10 CHECKING USERNAMES")

current_users = ['Stefan', 'viggo', 'rebecca', 'Herman', 'isac']
new_users = ['viggo', 'emil', 'hedda', 'calle', 'Herman']

#list comprehension!!
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users_lower:
		print(f'Sorry {new_user.title()}, that name is taken.')
	else:
		print(f'Great {new_user.title()} is still availible.')

print("\n5-11 ORDINAL NUMBERS")
numbers = list(range(1,10))

for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(f'{number}th')