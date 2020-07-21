print('\n########## Simple dictionary ############')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

print('\n########## Accessing Values ############')

new_points = alien_0['points']
print(f'You just earned {new_points} points!')

print('\n########## adding new kye value pairs ############')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('\n########## Starting with an empty dictionary ############')

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

print('\n########## Modifying values in a dictionary ############')
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color'].upper()}")

print('\n########## Track speed of moving alien ############')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original y_position: {alien_0['x_position']}")

#Move the alien to the right
#Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be a fast alien
	x_increment = 3

# the new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

print('\n########## Removing Key-Value pairs - del to delete ############')
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


####### NESTING ###########
print('\n########## NESTING ############')
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

print('\n#### Store the alien dictionaries in a list called alien')
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

print('\n#### use range() to create 30 aliens')
aliens = []

#make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

# show how many aliens we created
print(f"Total number of aliens created: {len(aliens)}")

print('\n#### change the values of the first three aliens')

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
 # show the first five aliens
for alien in aliens[:5]:
 	print(alien)
print("...")

print('\n#### change the values of every second alien from 10 - 30 ')

for alien in aliens[:]:
	if alien['color'] == 'green':
		alien['color'] = 'blue'
for alien in aliens[:]:
 	print(alien)
print("...")

print('\n#### with elif')

for alien in aliens[:]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 10
		alien['speed'] = 'medium'
	elif alien['color'] == 'yellow':
			alien['color'] = 'red'
			alien['points'] = 15
			alien['speed'] = 'fast'
 # show the first five aliens
for alien in aliens[:10]:
 	print(alien)
print("...")