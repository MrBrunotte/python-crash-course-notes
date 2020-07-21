print('\n########## Using get() to access Values ############')
alien_0 = {'color':'green', 'speed': 'slow'}
# we get KeyError when we want to print a key value that doesnt exist!
#print(alien_0['points'])
point_value = alien_0.get('points', 'No point value assigned!')
print(point_value)
# leaving out the second argument in the get() will return the value None
point_value = alien_0.get('points')
print(point_value)