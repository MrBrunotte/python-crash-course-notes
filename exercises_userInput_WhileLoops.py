

# message = input("What is your age? ")
# print(message)
# print(type(message))
# message = int(message)
# print(message)
# print(type(message))

# 7.1 - Rental Car
excercise = "7.1 - Rental Car"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# rental_car = input("What kind of rental car would you like? ")
# print(f"Let me see if we have any {rental_car.title()}s available!")

# 7.2 - Restaurant seating
excercise = "7.2 - Restaurant seating"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# seats = input("How many guests are you tonight? ")
# seats = int(seats)

# if seats >= 8:
#     print(
#         f"Since your party is {seats} persons, you will have to wait for a bigger table!")
# else:
#     print(f"Your party of {seats} are welcome to follow me to your table!")

# 7.3 - Multiples of Ten
excercise = "7.3 - Multiples of Ten"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# number = input(
#     "Please give me a whole number (integer), and I will tell you if it is multiple by 10 or not: ")
# number = int(number)

# if number % 10 == 0:
#     print(f"The number {number} IS multiple with 10.")
# else:
#     print(f"The number {number} IS NOT multiple with 10.")

# 7.4 - Pizza Toppings
excercise = "7.4 - Pizza Toppings"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


# prompt = "\n(Enter quit when you are finished adding toppings)"
# prompt += "\n\tWhat topping would you like on your pizza? add one: "

# while True:
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f"\n I'll add {topping.title()} to your pizza.")
#     else:
#         break


# 7.5 - Movie Tickets
excercise = "7. 5 - Movie Tickets"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# welcome = "--------- Welcome to the cinema! ---------\n"
# print(welcome.upper())
# price = "Ticketprices are as follows" + "\n\tUnder the age of 3 - Free" + \
#     "\n\tBetween the age of 3-12 - $10" + "\n\tOver the age of 12 - $15"
# print(price)

# age = input("\n\tso How old are you? ")
# age = int(age)

# active = True
# while active:
#     if age < 3:
#         print(f"\nSince you are {age} years old, the ticket is free")
#         active = False
#     elif age > 3 or age < 12:
#         print(f"\nSince you are {age} years old, the ticket cost $10")
#         active = False
#     elif age > 12:
#         print(f"\nSince you are {age} years old, the ticket cost $15")
#         active = False
#     else:
#         active = False


# 7.6 - Three exits
excercise = "7.6 - Three exits"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


# 7.8 Deli
excercise = "7.8 Deli"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# sandwich_orders = ['turkey', 'ham', 'cheese', 'tuna', 'crabsticks']
# finished_sandwiches = []

# print(f"The sandwich_orders list: {sandwich_orders}")
# print(f"The finished_orders list is empty: {finished_sandwiches}\n")

# while sandwich_orders:
#     sandwich = sandwich_orders.pop().title()
#     print(f"Your {sandwich} sandwich is done!")

#     finished_sandwiches.append(sandwich)

# print(f"\nThe sandwich_orders list is now empty: {sandwich_orders}")
# print(f"The finished_orders list is now filled: {finished_sandwiches}\n")

# print("The following sandwiches have been made.\n")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# 7.9 - No Pastrami
excercise = "7.9 - No Pastrami"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# sandwich_orders = ['turkey', 'pastrami', 'ham',
#                    'pastrami', 'cheese', 'pastrami', 'tuna', 'crabsticks']
# finished_sandwiches = []

# print(f"The sandwich_orders list: {sandwich_orders}")
# print(f"The finished_orders list is empty: {finished_sandwiches}\n")

# print("We are out of Pastrami!")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print(f"The sandwich_orders list: {sandwich_orders}")
# print("\n")

# while sandwich_orders:
#     sandwich = sandwich_orders.pop().title()
#     print(f"Your {sandwich} sandwich is done!")

#     finished_sandwiches.append(sandwich)

# print(f"\nThe sandwich_orders list is now empty: {sandwich_orders}")
# print(f"The finished_orders list is now filled: {finished_sandwiches}\n")

# print("The following sandwiches have been made.\n")
# for finished_sandwich in finished_sandwiches:
#     print(finished_sandwich)

# 7.10 - Dream Vacation
excercise = "7.10 - Dream Vacation"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n"),

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Where is your dream vacation? ")

    responses[name] = response

    repeat = input("Let another person take the poll?? (y/n) ")
    if repeat == 'n':
        polling_active = False

print("\n#--- RESULTS ---#\n")
for name, response in responses.items():
    print(f"{name.title()} would like to vacation in: {response.upper()}.")
