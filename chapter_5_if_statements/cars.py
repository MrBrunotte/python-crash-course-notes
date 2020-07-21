print("Check for EQUALITY == ")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

print("\nCheck for Inequality !=")

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
	print("Hole the anchovies!")

## Checking multipel conditions
print("\nMULTIPLE CONDITIONS")
age_0 = 22
age_1 = 19

if age_0 >= 21 and age_1 >= 21:
	print('Your age is under 21!')
else:
	print('Both ages are not under 21')

## checking if a VALUE is in a list
requested_toppings = ['mushrooms', 'pepperoni', 'onions', 'pineapple']
topping = 'pepperoni'

if topping in requested_toppings:
	print(f'{topping.title()} is in the toppings')

## checking if a VALUE is NOT in a list
requested_toppings = ['mushrooms', 'pepperoni', 'onions', 'pineapple']
topping = 'garlic'

if topping not in requested_toppings:
	print(f'{topping.title()} is not in the toppings')

#checking for specila items
## checking if a VALUE is in a list
print("\nChecking for special items")
requested_toppings = ['mushrooms', 'pepperoni', 'onions', 'pineapple']

for requested_topping in requested_toppings:
	if requested_topping == 'pepperoni':
		print("Sorry! We are out of pepperoni right now.")
	else:
		print(f'Adding {requested_topping}.')
print("\nFinished making your pizza!")

print("\nChecking that a list is not empty")
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print:print(f'Adding {requested_topping}.')
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")	


#USING MULTIPLE LISTS
print("USING MULTIPLE LISTS")
availible_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french freis', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in availible_toppings:
		print(f'Adding "{requested_topping.title()}".')
	else:
		print(f'Sorry, we don´t have "{requested_topping.title()}"')
print("\nFinished making your pizza")