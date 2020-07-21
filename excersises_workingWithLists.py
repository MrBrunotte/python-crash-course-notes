# 4.1 - Pizzas
excercise = "4.1 - Pizzas"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

pizzas = ['cappicciosa', 'hawaii', 'calzone', 'pepperoni']
for pizza in pizzas:
    print(f"{pizza.title()} is one of our four pizzas!")
print("\nI really love these pizzas")

# 4.2 - Animals
excercise = "4.2 - Animals"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

animals = ['dogs', 'cats', 'parrots', 'gold fisch']
for animal in animals:
    print(animal.title() + '\n')

for animal in animals:
    print(f"{animal.title()} are great pets!")
print("\nAll of these animals are pets.")

# 4.3 - Counting to twenty
excercise = "4.3 - Counting to twenty"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

for num in range(1, 21):
    print(num)

# 4.4 - One Million
excercise = "4.4 - One Million"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

print("Commented out because it takes to long!")
# million = list(range(1, 1_000_001))
# for number in million:
#     print(number)

# 4.5 - Summing a Million
excercise = "4.5 - Summing a Million"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

million = list(range(1, 1_000_001))
print(min(million))
print(max(million))
print(sum(million))

# 4.6 - Odd numbers
excercise = "4.6 - Odd numbers"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

odd_numbers = list(range(1, 21, 2))
print("Each number:")
for odd in odd_numbers:
    print(f"{odd} is an odd number!")
print(f"\nThese are the odd numbers in my list:\n {odd_numbers}")

# 4.7 - Threes
excercise = "4.7 - Threes"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

multiples = list(range(3, 31, 3))
print(multiples)
for num in multiples:
    print(num)
print(multiples)

# 4.8 - Cubes
excercise = "4.8 - Cubes"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

cubes = list(range(1, 11))
for cube in cubes:
    print(cube**3)

# 4.9 - Cube Comprehension
excercise = "4.9 - Cube Comprehension"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

print("The for loop as a List comprehension")
cubes = list(range(1, 11))
cubes = [cube**3 for cube in cubes]
print(cubes)

# 4.10 - Slices
excercise = "4.10 - Slices"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

long_list = ['stefan', 'rebecca', 'viggo',
             'pappa', 'hedda', 'isac', 'herman']
print(len(long_list))
print("\nThese are the first three people in the list:")
for people in long_list[:3]:
    print(people.title())

print(f"\nThis is the orignal list: {long_list}")
print("\nthese are the three people in the middle:")
for people in long_list[2:5]:
    print(people.title())

print(f"\nThis is the orignal list: {long_list}")
print("\nThese are the last three people in the list:")
for people in long_list[-3:]:
    print(people)

# 4.11 - My pizzas, Your pizzas
excercise = "4.11 - My pizzas, Your pizzas"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

friend_pizzas = pizzas[:]
print(friend_pizzas)
pizzas.append('margaritha')
friend_pizzas.append('kebab pizza')
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza.title())

uppercase_letters = "\nMy friends favourite pizzas are:"
print(uppercase_letters.upper())
for pizza in friend_pizzas:
    print(pizza.title())

# 4.12 - More Loops
excercise = "4.12 - More Loops"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# 4.13 - Buffet
excercise = "4.13 - Buffet"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

foods = ('fish', 'egg nog', 'meat', 'pancakes', 'strudel')
for food in foods:
    print(food.title())

print("\nOver written Tuple:")
foods = ('oysters', 'egg nog', 'hamburger', 'pancakes', 'strudel')
for food in foods:
    print(food.title())
