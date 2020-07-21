print("\n########## the input() function ############")
name = input("Please tell me your name: ")
print(f"\nHello {name}")

print("\n######### prompt several lines #############")
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}")
