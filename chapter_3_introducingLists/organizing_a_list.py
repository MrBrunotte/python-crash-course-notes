# sort()
print('sorting a list PERMANENTLY with sort()')
cars = ['honda', 'volvo', 'ford', 'mercedes', 'opel', 'tesla']
print(cars)
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# sorted()
print('\n\nSorting a list TEMPORARILY with sorted()')
cars = ['honda', 'volvo', 'ford', 'mercedes', 'opel', 'tesla']
print(cars)
print(f'{sorted(cars)} sorted temporarily')
print(f'{cars} back to original order')
cars.sort()
print(f'{cars} sorted premanently')
cars.sort(reverse=True)
print(f'{cars} reversed order')

# reverse()
print('\n\nPrinting a list in revere order with reverse()')
cars = ['honda', 'volvo', 'ford', 'mercedes', 'opel', 'tesla']
print(f'{cars} original order')
cars.reverse()
print(f'{cars} in reversed order')

# finding length of list
print('\n\nFinding length of list with len()')
cars = ['honda', 'volvo', 'ford', 'mercedes', 'opel', 'tesla']
print(f'{cars} original order')

print(len(cars))
