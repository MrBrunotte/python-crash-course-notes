print("\n########## the input() function ############")
# message =  input("Tell me something, and I will repeat it back to you: ")
# print(message)

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

print("\n########## Using a Flag ############")
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("Game over!")
    else:
        print(message)
