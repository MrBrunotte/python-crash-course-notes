# 3-1 Names
print('\n\n3-1 NAMES')
names = ['calle', 'nordin', 'erik', 'björne']
print(names[0].capitalize())
print(names[1].capitalize())
print(names[2].capitalize())
print(names[3].capitalize())

# 3-2 Greetings
print('\n\n3-2 GREETINGS')
message = 'Hello there, '
print(f'{message}{names[0].capitalize()}!')
print(f'{message}{names[1].capitalize()}!')
print(f'{message}{names[2].capitalize()}!')
print(f'{message}{names[3].capitalize()}!')

# 3-3 Your own list
print('\n\n3-3 YOUR OWN LIST')
cars = ['Lambo', 'Ferrari', 'Bentley', 'Mercedes']
message = 'I would really like to own a '
print(f'{message}{cars[0]}!!!')
print(f'{message}{cars[1]}!!!')
print(f'{message}{cars[2]}!!!')
print(f'{message}{cars[3]}!!!')

# 3-4 Guest list
print('\n\n3-4 GUEST LIST')
dinner_guests = ['bob marley', 'pappa', 'viggo']
print(f'Hey {dinner_guests[0].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[1].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[2].title()} I would like to invite you to dinner!')

# 3-5 Changing Guest
print('\n\n3-5 CHANGING GUESTS')
dinner_guests = ['bob marley', 'pappa', 'viggo']
print(f'Hey {dinner_guests[0].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[1].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[2].title()} I would like to invite you to dinner!')
print(
    f'{dinner_guests[0].title()} is not able to make it, someone will have to take his place!')
del dinner_guests[0]
dinner_guests.append('peter pan')
print(dinner_guests)
print(f'Hey {dinner_guests[0].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[1].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[2].title()} I would like to invite you to dinner!')

# or
print('\nOR I CAN DO IT LIKE THIS:')
dinner_guests = ['bob marley', 'pappa', 'viggo']
print(dinner_guests)
print(
    f'{dinner_guests[0].title()} is not able to make it, someone will have to take his place!')
dinner_guests[0] = 'peter pan'
print(f'Hey {dinner_guests[0].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[1].title()} I would like to invite you to dinner!')
print(f'Hey {dinner_guests[2].title()} I would like to invite you to dinner!')

print(
    f'Hey {dinner_guests[0].title()}, {dinner_guests[1].title()}, {dinner_guests[2].title()} you all are now invited to the dinner!')

# 3-6 More Guests
print('\n\n3-6 MORE GUESTS')
print(dinner_guests)
dinner_guests.insert(0, 'erik')
dinner_guests.insert(2, 'peter')
dinner_guests.append('fredde')
print(f'{dinner_guests} you are now invited to dinner')

# 3-7 Shrinking guest list
print('\n\n3-7 SHRINKING GUEST LIST')
print(f'{dinner_guests} you are now invited to dinner')
print('Im sorry guys! I can only invite two people for dinner')
popped_guest = dinner_guests.pop()
print(f'{popped_guest} Im sorry I cant invite you to dinner anymore!')
popped_guest = dinner_guests.pop()
print(f'{popped_guest} Im sorry I cant invite you to dinner anymore!')
popped_guest = dinner_guests.pop()
print(f'{popped_guest} Im sorry I cant invite you to dinner anymore!')
popped_guest = dinner_guests.pop()
print(f'{popped_guest} Im sorry I cant invite you to dinner anymore!')
print(f'{dinner_guests[0]} and {dinner_guests[1]} you are still invited!')
print(dinner_guests)
del dinner_guests[0]
del dinner_guests[0]
print(dinner_guests)

# 3-8 Seeing the world
print('\n\n3-8 SEEING THE WORLD')
locations = ['Australia', 'Grand Canyon', 'Amazonas', 'Antibes', 'Lake Como']
print(f'\nLocations I want to visit:\n{locations}')
# sorted locations temporarily
print(f'\nLocations sorted alphabetically TEMPORARILY: \n{sorted(locations)}')
print(f'\nBack to original list: \n{locations}')
# sorted in reveresed alphabetical order temporaily
print(
    f'\nLocations in reversed alphabetically order TEMPORARILY: \n{sorted(locations, reverse=True)}')
print(f'\nBack to original list: \n{locations}')
# reverse()
locations.reverse()
print(f'\nLocations in reversed order: \n{locations}')
locations.sort()
print(f'\nLocations sorted order: \n{locations}')
locations.sort(reverse=True)
print(f'\nLocations in reversed order: \n{locations}')

# 3-9 length
print('\n\n3-9 LENGTH OF DINNER GUEST LIST')
print(f'I ended up inviting: "{len(dinner_guests)}" guest for dinner')

# 3-10 every function
print('\n\n3-10 EVERY FUNCTION')
every_function = ['sweden', 'denmark',
                  'norway', 'finland', 'germany', 'bahamas']
print(every_function[3])
print(every_function[3].title())
print(every_function[-1].upper())
print(every_function[1].capitalize())
print(f'My mother lives in the {every_function[-1].title()}')
print(every_function)
every_function[0] = 'sverige'
print(every_function)
every_function.append('uk')
print(every_function)
every_function.insert(3, 'us')
print(every_function)
del every_function[3]
print(every_function)
popped_country = every_function.pop()
print(popped_country)
print(every_function)
second_popped_country = every_function.pop(2)
print(second_popped_country)
print(every_function)
removed_country = every_function.remove('finland')
print(every_function)
print(sorted(every_function))
every_function.reverse()
print(every_function)
every_function.sort()
print(every_function)
every_function.sort(reverse=True)
print(every_function)
print(len(every_function))
