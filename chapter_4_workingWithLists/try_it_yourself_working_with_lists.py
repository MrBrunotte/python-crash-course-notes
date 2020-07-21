# 4-1 Pizzas

print("4-1 PIZZAS")

pizzas = ['calzone', 'margaritha', 'vesuvio']

for pizza in pizzas:
	print(f"pizza name: {pizza.title()}")
print("\tThey are all very tasty!\n\tBut they are not that healthy\n\tSo don't eat to many!!")


# 4-2 Animals

print("\n4-2 ANIMALS")

animals = ['lion', 'elephant', 'zebra']

for animal in animals:
	print(f"\t{animal}s live in Afica")
print("\tThey are all wild animals!")

# 4-3 Counting to twenty
print("\n4-3 COUNTING TO TWENTY")

one_to_twenty = list(range(1,21))
print(one_to_twenty)

# 4-4 One million
print("\n4-4 ONE MILLION")

#million = list(range(1,1_000_001))
#print(million)

# 4-5 Summing a million
print("\n4-5 SUMMING A MILLION")

numbers = list(range(1,1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6 Odd numbers
print("\n4-6 ODD NUMBERS")

odd_numbers = list(range(1,21,2))
print(odd_numbers)

# 4-7 Threes
print("\n4-7 THREES")

threes = [value for value in range(3,31,3)]
print(threes)

# 4-8 CUBES
print("\n4-8 CUBES")

cubes = [value**3 for value in range(1,11)]
print(cubes)

# 4-8 CUBES
print("\n4-8 CUBES another way")

cubes = []
for number in range(1,11):
	cube = number**3
	cubes.append(cube)
print(cubes)

# 4-8 CUBES
print("\n4-8 CUBES yet another way")

cubes = []
for number in range(1,11):
	cubes.append(number**3)
print(cubes)

# 4-9 Cube comprehension
print("\n4-9 CUBE COMPREHENSION")

cubes = [num**3 for num in range(1,11)]
print(cubes)

for cube in cubes:
	print(cube)

# 4-10 Slices
print("\n4-10 SLICES")

list_items = [1,2,3,4,5,6,7,8,9,10]
print(f"first three items in the list_items are: \n\n\t{list_items[0:3]}\n\t")
print(f"Three items from the middle in the list_items are: \n\n\t{list_items[3:6]}\n\t")
print(f"last three items in the list_items are: \n\n\t{list_items[-3:]}\n\t")

# 4-11 My pizzas, your pizzas
print("\n4-11 MY PIZZAS, YOUR PIZZAS")

pizzas = ['calzone', 'margaritha', 'vesuvio']
# make a copy of list to friends_list
friend_pizzas = pizzas[:]
# add new pizza 
pizzas.append('hawaii')
friend_pizzas.append('cacciatore')

print("My favourite pizzas are:")
for pizza in pizzas:
	print(f'\t- {pizza}')

print("My friend's favourite pizzas are:")
for pizza in friend_pizzas:
	print(f'\t- {pizza}')

# 4-12 More loops
print("\n4-12 MORE LOOPS")

my_foods = ['pizza', 'hamburger', 'falafel', 'carrot cake']
for pizza in my_foods:
	print(f'- {pizza}')

# 4-13 TUPLES buffet
print("\n4-12 BUFFET (TUPLES)")
five_foods = ('cereal', 'cake', 'fish', 'meat', 'vegeterian')
for food_item in five_foods:
	print(f'- {food_item}')
print('\n')

# You cannot modify a tulip! but you can overwrite it
#five_foods[3] = 'meat'

# replace the elements in the tulip
print("We just changed our menu!")
five_foods = ('hamburger', 'french fries', 'coca cola', 'coffee', 'tee')
for food_item in five_foods:
	print(f'- {food_item}')
print('\n')