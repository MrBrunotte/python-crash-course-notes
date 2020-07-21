# 3.1 - Names
excercise = "3.1 - Names"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# print each name in the family, one at a time.
print("This is my family:")
names = ['rebecca', 'stefan', 'viggo', 'hedda']
for name in names:
    print(name.title())
# print the list
print(names)

# 3.2 - Greetings
excercise = "3.2 - Greetings"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

for name in names:
    print(f"Family member name: {name.title()}")

# 3.3 - Your Own List
excercise = "3.3 - Your Own List"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

transports = ["plane", "car", "motorcycle", "yacht"]

for item in transports:
    print(f"I would like to own my own {item.upper()}!")
print("I don't own them yet but when my crypto's get going I will!!")

# 3.4 - Guest list
excercise = "3.3 - Guest list"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

dinner_guests = ["pappa", "bob marley", "farfar"]

for guest in dinner_guests:
    print(f"{guest.title()}, I really would like to invite you to dinner!!")

# 3.5 - Changeing Guest List
excercise = "3.5 - Changeing Guest List"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

for guest in dinner_guests:
    print(f"{guest.title()}, I really would like to invite you to dinner!!")
cannot_show = dinner_guests[2]
# Farfar cant make it to dinner
print("\n" + cannot_show.title() + ", can't make it to the dinner!\n")
# replace farfar with Omi
dinner_guests[2] = "omi"
for guest in dinner_guests:
    print(f"{guest.title()}" + ", You are now invited!")

# 3.6 - More guests
excercise = "3.6 - More guests"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

for guest in dinner_guests:
    print(f"{guest.title()}" + ", You are now invited!")
print("I just found a bigger table so more people will join us to dinner!!")

dinner_guests.insert(0, "olof palme")
print(dinner_guests)

dinner_guests.insert(2, "farfar")
print(dinner_guests)

dinner_guests.append("sitting bull")
print(dinner_guests)

for guest in dinner_guests:
    print(f"{guest.title()}" + ", you are invited to the dinner of all DINNERS!")

# 3.7 - Shrinking Guest List
excercise = "3.7 - Shrinking Guest List"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

print("I'm sorry, but the table is delayed so I can only invite two people to dinner!")
# print lenght of dinner_guests
print(len(dinner_guests))
# remove and assign popped guest to the popped_guest variable and print message
popped_guest = dinner_guests.pop()
print(f"{popped_guest.title()}" +
      ", unfortunately there is no room at the table for you!\n")
popped_guest = dinner_guests.pop()
print(f"{popped_guest.title()}" +
      ", unfortunately there is no room at the table for you!\n")
popped_guest = dinner_guests.pop()
print(f"{popped_guest.title()}" +
      ", unfortunately there is no room at the table for you!\n")
popped_guest = dinner_guests.pop()
print(f"{popped_guest.title()}" +
      ", unfortunately there is no room at the table for you!\n")
print(len(dinner_guests))
# print individual message to last two invitees
print(dinner_guests)
for name in dinner_guests:
    print(f"{name.title()}, you are still invited!")

# Delete the last two persons
print(dinner_guests)
del dinner_guests[1]
print(dinner_guests)
del dinner_guests[0]
print(dinner_guests)

# 3.8 - Seeing the world
excercise = "3.8 - Seeing the world"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

locations = ['hawaii', 'the alps', 'australia', 'new zeeland', 'the amazon']
print(locations)

# sorted() function (temporarily)
print(f"\nLocations in sorted order: \n{locations}")
print(sorted(locations))
sorted_locations = sorted(locations)
print(sorted_locations)
print(f"\nLocations back to original order: \n{locations}")
print(locations)

# reverse() function in reverse (permanently)
print(f"\nLocations in reversed order: {locations}")
locations.reverse()
print(f"\nLocations in reverse back to original order: \n{locations}")
locations.reverse()
print(locations)

# sort() function (permanently)
print(f"\nThe sort() sorts the list permanently: \n{locations}")
locations.sort()
print(locations)
print(f'\nLocations in reversed order: \n{locations}')
locations.sort(reverse=True)
print(locations)

# 3.9 - Dinner Guests
excercise = "3.9 - Dinner Guests"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

dinner_guests = ["pappa", "bob marley", "farfar"]

print(f"The are {len(dinner_guests)} dinner guests!")
print(f"And the dinner guests are: \n{dinner_guests}")

# 3.10 - Every Function
excercise = "3.10 - Every Function"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

fruits = ['banana', 'apple', 'guava', 'pear',
          'orange', 'melon', 'papaya', 'mango']
print(fruits)
print("\nAccessing Elements in a list")
print(fruits[3].title())
print(fruits[-1].title())
print("\n Using individual values from a list")
print(f"The fruits I like best are: \n\t{fruits[1]} \nand \n\t{fruits[-1]}")

print("\nAdding grapes to the list:\n")
fruits.append("grapes")
print(fruits)

print("\nInserting blueberries at index 4 in the list:\n")
fruits.insert(4, "blueberries")
print(fruits)
print(fruits[4])

print("\nRemove element using del()\n")
print(fruits)
print(fruits[-1])
del fruits[-1]
print(fruits)

print("\nRemove element using pop()\n")
print(fruits)
popped_fruit = fruits.pop()
print(popped_fruit)
print(fruits)

print("\nRemove specific index element using pop()\n")
print(fruits)
popped_fruit = fruits.pop(2)
print(popped_fruit)
print(fruits)

print("\nRemove item by value\n")
print(fruits)
fruits.remove('orange')
print(fruits)

print("\nSort list temporarily with sorted() Function\n")
print(fruits)
print(sorted(fruits))
print(fruits)

print("\nSort list permantly with sort() Method\n")
print(fruits)
fruits.sort()
print(fruits)

print("\nPrinting a list in reversed order\n")
print(fruits)
fruits.reverse()
print(fruits)

print("\nFinding length of list\n")
print(len(fruits))
