# Slicing a list
print("SLICING A LIST [0:3]")

players =  ['charles', 'martina', 'michael', 'florence', 'eli', 'peter']
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[2:])
print(players[-3:])
print(players[0:5:2])

print("\nHere are the first three players on my team: ")
for player in players[:3]:
	print(player.title())

