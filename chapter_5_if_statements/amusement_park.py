age = 12
if age < 4:
	print("Your admission is free")
elif age < 18:
	print("Your admission cost is $25")
else:
	print("Your admission cost is $40")

print("\nBetter way to do this is to put price inse the condition\n")
age = 12
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print(f"Your admission cost is ${price}")

print("\nBetter way to do this is to put price inse the condition without else\n")
age = 70
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age >=65:
	price = 40
print(f"Your admission cost is ${price}")

# Multiple if statements
print("\nMULTIPLE IF STATEMENTS\n")
toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in toppings:
	print("Adding mushrooms")
if 'pepperoni' in toppings:
	print("Adding pepperoni")
if 'extra cheese' in toppings:
	print("Adding extra cheese")

print('\nFinishing your pizza!')