# 10.3 - Guests
import json
excercise = "10.3 - Guests"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# name = input("What's your name? ")

# filename = 'guest.txt'

# with open(filename, 'w') as f:
#     f.write(name.title())

# 10.4 - Guest Book
excercise = "10.4 - Guest Book"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# filename = 'guest_book.txt'

# print("Enter 'quit' when you are finished.")
# while True:
#     name = input("\nWhat's your name? ")
#     if name == 'quit':
#         break
#     else:
#         with open(filename, 'a') as f:
#             f.write(f"{name.title()}\n")
#         print(f"Hi {name.title()}, you've been added to the guest book.")

# 10.5 - Programming Poll
excercise = "10.5 - Programming Poll"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# filename = 'programming_poll.txt'

# responses = []
# while True:
#     response = input("\nWhy do you like programming? ")
#     responses.append(response)

#     continue_poll = input("Would you like to let someone else respond? (y/n) ")
#     if continue_poll != 'y':
#         break
# # append 'a' the poll to the file
# with open(filename, 'a') as f:
#     for response in responses:
#         f.write(f"{response}\n")

# 10.6 - Addition
excercise = "10.6 - Addition"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# try:
#     x = input("Give me a number: ")
#     x = int(x)

#     y = input("Give me another number: ")
#     y = int(y)
# except ValueError:
#     print("Sorry, I really needed a number.")
# else:
#     sum = x + y
#     print(f"The sum of {x} and {y} is {sum}.")


"""
This is what the traceback error looks like when giving a letter instead of a number!
Traceback (most recent call last):
  File "d:\Desktop\DEVELOPMENT_LEARNING\PYTHON_CRASH_COURSE\python_work\exercises_files.py", line 63, in <module>
    y = int(y)
ValueError: invalid literal for int() with base 10: 'i'
"""


# 10.7 - Addition Calculator
excercise = "10.7 - Addition Calculator"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# print("Enter 'q' at any time to quit.\n")

# while True:
#     try:
#         x = input("\nGive me a number: ")
#         if x == 'q':
#             print("Thanks for trying!")
#             break

#         x = int(x)

#         y = input("Give me another number: ")
#         if y == 'q':
#             print("Thanks for trying!")
#             break

#         y = int(y)

#     except ValueError:
#         print("Sorry, I really needed a number.")

#     else:
#         sum = x + y
#         print(f"The sum of {x} and {y} is {sum}.")

# 10.8 - Cats and Dogs
excercise = "10.8 - Cats and Dogs"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# filenames = ['cats.txt', 'dogss.txt']

# for filename in filenames:
#     print(f"\nReading file: {filename}")
#     try:
#         with open(filename) as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print(
#             f"\n\tSorry, I can't find the file you call: {filename} \n\tPlease check your spelling.")

# 10.9 - Silent Cats and Dogs
excercise = "10.9 - Silent Cats and Dogs"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# filenames = ['cats.txt', 'dogs.txt']

# for filename in filenames:

#     try:
#         with open(filename) as f:
#             contents = f.read()

#     except FileNotFoundError:
#         pass

#     else:
#         print(f"\nReading file: {filename}")
#         print(contents)

# 10.10 - Common Words
excercise = "10.10 - Common Words"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")

# title = 'Alice in wonderland'
# print(title.split())
# print(len(title))


# 10.11 - Favorite Number
excercise = "10.11 - Favorite Number"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")
