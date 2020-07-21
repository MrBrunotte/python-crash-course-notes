print("\n### Filling a dictionary with user input ###")

responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # ask for the users name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb on Sunday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input(
        "Would you like to let another person respond? (y / n) ")
    if repeat == 'no':
        polling_active = False

# polling is complete. Show results.
print("\n----- Poll results -----")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
