print("\n######### 7-1 Rental Car #############")
# prompt = "Dear customer, "
# prompt += "What kind of rental car would you like? "
# car = input(prompt)

# print(f"\nLet me see if I can find you a {car.title()}.")

print("\n######### 7-2 Restaurant seating #############")
# dinner_guests = input("How many dinner guests are in your party? ")
# dinner_guests = int(dinner_guests)

# if dinner_guests > 8:
#     print(
#         f"\nYour party is quite large, you'll have to wait a bit for a table for {dinner_guests} people.")
# else:
#     print(f"\nYour table for {dinner_guests} is ready, please follow me!")

print("\n######### 7-3 Multiple of ten #############")
# number = input(
#     "Lets see if your number is a multiple of 10! Please add number: ")
# number = int(number)

# if number % 10 == 0:
#     print(f"The {number} is a multiple of 10")
# else:
#     print(f"The {number} is not a multiple of 10")

print("\n######### 7-4 Pizza Toppings #############")
# prompt = "\n(type 'quit' when you are finished adding toppings). "
# prompt += "\nPlease add a topping for your pizza: "

# while True:
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f"{topping.title()} will be added to your pizza!")
#     else:
#         break

print("\n######### 7-5 Movie tickets #############")
# prompt = "\n(type 'quit' to quit). "
# prompt += "\nWhat is your age?: "

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("\tYou get in free!")
#     elif age < 13:
#         print("\tYour ticket is $10")
#     else:
#         print("\tYour ticket is $15")

print("\n######### 7-6 Three exits #############")
print("### Use a conditional test in the while statement to stop the loop")
# prompt = "\n(type 'quit' when you are finished adding toppings). "
# prompt += "\nPlease add a topping for your pizza: "

# topping = ""
# while topping != 'quit':
#     topping = input(prompt)

#     if topping == 'quit':
#         print("\twe used a conditional test to stop the loop")


print("### Use an active variable (flag PAGE: 120) to control how long the loop runs.")
# prompt = "\n(type 'quit' when you are finished adding toppings). "
# prompt += "\nPlease add a topping for your pizza: "

# active = True

# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#         print(f"Thanks and goodbye We used a Flag (an activ variable) to quit the program")
#     else:
#         print(f"{message.title()} will be added!")

print("### Use a break statement to exit the loop when the user enters a 'quit' value")
# prompt = "\n(type 'quit' when you are finished adding toppings). "
# prompt += "\nPlease add a topping for your pizza: "

# while True:
#     topping = input(prompt)

#     if topping != 'quit':
#         print(f"{topping.title()} will be added to your pizza!")
#     else:
#         print("We used the break statement to end the program here")
#         break

print("\n######### 7-8 Deli #############")
# # make a list
# sandwich_orders = ['turkey', 'tuna', 'veggie',
#                    'meatballs', 'el diablo', 'sandy']
# # maka an empty list
# finished_sandwiches = []
# print(sandwich_orders)
# print(finished_sandwiches)

# # loop through the sandwich_orders list with a message
# while sandwich_orders:
#     orders = sandwich_orders.pop()
#     print(f"I'm workding on your {orders} sandwich!")
#     finished_sandwiches.append(orders)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich.title()} sandwich")

print("\n######### 7-9 No Pastrami #############")
# sandwich_orders = ['turkey', 'tuna', 'veggie',
#                    'meatballs', 'el diablo', 'sandy']
# print(sandwich_orders)
# sandwich_orders.append('pastrami')
# sandwich_orders.append('pastrami')
# sandwich_orders.append('pastrami')
# finished_sandwiches = []
# print(sandwich_orders)
# print(finished_sandwiches)

# print("i'm sorry, we're all out of pastrami today.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# print("\n")
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop()
#     print(f"I'm working on your {current_sandwich.title()} sandwich.")
#     finished_sandwiches.append(current_sandwich)

# print("\n")
# for sandwich in finished_sandwiches:
#     print(f"I made a {sandwich.title()} sandwich")

print("\n######### 7-10 Dream Vacation #############")
name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the world, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name:place}
responses = {}

while True:
    # ask the user where they like to go
    name = input(name_prompt)
    place = input(place_prompt)

    # store the response
    responses[name] = place

    # ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break

# show results of the survey
print("\n---- Results ----")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
