prompt = "\n(type 'quit' when you are finished adding toppings). "
prompt += "\nPlease add a topping for your pizza: "

while True:
    topping = input(prompt)

    if topping != 'quit':
        print(f"{topping.title()} will be added to your pizza!")
    else:
        break