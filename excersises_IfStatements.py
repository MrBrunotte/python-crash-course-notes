# 5.1 - Conditional Test (Boolean test)
excercise = "5.1 - Conditional Test (Boolean test)"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

car = 'Subaru'
print(car)
print("Is car == 'Subaru'? I predict True")
print(car == 'Subaru')
print("Is car == 'subaru'? I predict False")
print(car == 'subaru')
print("Is car.lower() == 'subaru'? I predict True")
print(car.lower() == 'subaru')

animal = 'horse'
print(animal)
print("Is animal == 'Horse'? I predict False")
print(animal == 'Horse')
print("Is animal == 'horse'? I predict True")
print(animal == 'horse')
print("Is animal.upper() == 'Horse'? I predict True")
print(animal.upper() == 'Horse')

# 5.3 - Alien Colors
excercise = "5.3 - Alien Colors"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

print('\nThis test will pass so I will get an output!!')
alien_color = 'green'
print(f"The color of the alien is: {alien_color}")
if alien_color == 'green':
    print("The color of the Alien is Green and you earned 5 points")

print('\nThis test fails so I will get no output!!')
alien_color = 'red'
print(f"The color of the alien is: {alien_color}")
if alien_color == 'green':
    print("The color of the Alien is Green and you earned 5 points")

alien_color = 'green'
print(f"The color of the alien is: {alien_color}")
if alien_color == 'green':
    print("The Alien is GREEN")
else:
    print('The Alien is not green')

# 5.4 - Alien colors #2
excercise = "5.4 - Alien colors #2"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

alien_color = 'green'
print(f"The color of the alien is: {alien_color}")
if alien_color == 'green':
    print(f"{alien_color}! You just earned 5 points!\n")
else:
    print("The Alien is not Green! So you earned 10 points!\n")

alien_color = 'red'
print(f"The color of the alien is: {alien_color}")
if alien_color == 'green':
    print(f"{alien_color}! You just earned 5 points!\n")
else:
    print("The Alien is not Green! You just earned 10 points!")

# 5.5 - Alien Colors #3
excercise = "5.5 - Alien Colors #3"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

alien_color = 'green'
if alien_color == 'green':
    print("Green! You earned 5 points\n")
elif alien_color == 'yellow':
    print("Yellow! You earned 10 points\n")
else:
    print("Red! You earned 15 points\n")

alien_color = 'yellow'
if alien_color == 'green':
    print("Green! You earned 5 points\n")
elif alien_color == 'yellow':
    print("Yellow! You earned 10 points\n")
else:
    print("Red! You earned 15 points\n")

alien_color = 'red'
if alien_color == 'green':
    print("Green! You earned 5 points\n")
elif alien_color == 'yellow':
    print("Yellow! You earned 10 points\n")
else:
    print("Red! You earned 15 points\n")

# 5.6 - Stages of Life
excercise = "5.6 - Stages of Life"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

age = 48

if age < 2:
    print("You are a BABY!")
elif age <= 2 or age < 4:
    print("You are a TODDLER!")
elif age <= 4 or age < 13:
    print("You are a KID!")
elif age <= 13 or age < 20:
    print("You are a TEENAGER!")
elif age <= 20 or age < 65:
    print("You are an ADULT!")
else:
    print("You are an ELDER!")

# 5.7 - Favorite Fruit
excercise = "5.7 - Favorite Fruit"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

fruits = ['pineapple', 'apple', 'pear', 'mango', 'grapes', 'papaya', 'melon']

favorite_fruits = ['apple', 'kiwi', 'guava']

if 'pineapple' in fruits and 'apple' in favorite_fruits:
    print(f"You really like Pineapple and Apple")
else:
    print("They are not in both lists!")
if fruits[:2] != favorite_fruits[:2]:
    print("The three first fruits are not the same in the two lists")
if 'mango' in fruits or 'guava' in favorite_fruits:
    print(f"Mango is in the list 'fruits' and guava is in the list 'favorite_fruits'!")
if 'peach' in fruits:
    print(f"There are Peaches in the list")
else:
    print(f"There are no Peach in the list!")

# 5.8 - Hello Admin
excercise = "5.8 - Hello Admin"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

usernames = ['stefan', 'rebecca', 'admin', 'viggo', 'hedda']
print(usernames)

for name in usernames:
    if name == 'admin':
        print(f"Hello {name.title()}, would you like to see a status report?")
    else:
        print(f"Welcome back {name.title()}!")

# 5.9 - Nu Users
excercise = "5.9 - Nu Users"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

print(usernames)
del usernames[:]
#usernames = ['stefan']
#usernames = ['stefan', 'admin']

if usernames:
    for name in usernames:
        if name == 'admin':
            print(
                f"Hello {name.title()}, would you like to see a status report?")
        else:
            print(f"Welcome back {name.title()}!")
else:
    print(usernames)
    print("\nThe list is empty!\nWe need to find some more users!")

# 5.10 - Checking Usernames
excercise = "5.10 - Checking Usernames"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

current_users = ['stefan', 'Rebecca', 'Admin', 'viggo', 'Hedda']
new_users = ['isac', 'herman', 'Pappa', 'Viggo', 'Stefan']

# list comprehension
current_users_lower = [user.lower() for user in current_users]
print(current_users_lower)

# for loop
# current_users_lower = []
# for user in current_users:
#     current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username: '{new_user}' is already taken!")
    else:
        print(f"Great, the username: '{new_user}' is not taken!")

# 5.11 - Ordinal Numbers
excercise = "5.11 - Ordinal Numbers"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

numbers = list(range(1, 10))
print(numbers)

for num in numbers:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')
