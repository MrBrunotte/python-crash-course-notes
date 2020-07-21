dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# a tuple with only one element
my_small_typle = (3,)

#overwriting a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400,100)
print("\nModified dimensions")
for dimension in dimensions:
	print(dimension)