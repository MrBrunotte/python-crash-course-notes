bikes = ['cannondale', 'trek', 'redline', 'specialized']
print(bikes)

print(bikes[1])
print(bikes[0].capitalize())
print(bikes[-1].upper())

message = 'My first bike was a '
print(f'{message}{bikes[0].capitalize()}!')

# Modifying elements in a list
cars = ['honda', 'volvo', 'ford', 'mercedes', 'opel', 'tesla']
print(cars)

cars[1] = 'FERRARI'
print(cars)

# adding to a list - append()
cars.append('DODGE')
print(cars)

# append to empty list
fruit = []
fruit.append('apples')
print(fruit)
fruit.append('oranges')
print(fruit)
fruit.append('bananas')
print(fruit)

# use del when you dont need the item anymore.
# use pop() when you want to use the item after you 'popped' it from the list.

# del delete a position oranges [1]
del fruit[1]
print(fruit)

# remove with pop()
print(cars)
popped_cars = cars.pop()
print(cars)
print(popped_cars)

# remove with pop() from an index postion
print(cars)
popped_car = cars.pop(1)
print(cars)
message = f'I popped {popped_car.title()} from the cars list!'
print(popped_car)
print(message)

# remove an item by value
print(cars)
cars.remove('tesla')
print(cars)

# remove by value
name = 'stefan'
to_expensive = 'mercedes'
print(cars)
cars.remove(to_expensive)
print(cars)
print(f'The {to_expensive.title()} is to expensive for {name.title()}')
