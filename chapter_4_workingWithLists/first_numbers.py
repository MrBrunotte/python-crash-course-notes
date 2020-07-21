for value in range(5):
	print(value)

numbers = list(range(1,10))
print(numbers)

even_numbers = list(range(0,10,2))
print(even_numbers)

squares = []
for value in range(1,11):
	square = value ** 2
	squares.append(square)

print(squares)

# less code, skip the sqare variable
squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

# simple statistic with list of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List comprehension
