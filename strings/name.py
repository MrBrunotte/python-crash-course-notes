name = ('ada lovelace')
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'stefan'
last_name = 'brunotte'
full_name = f'{first_name} {last_name}'
print(full_name)
print(f'Hello, {full_name.title()}!')

message = f'Hello, {full_name.title()}!'
print(message)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

# to remove whitespace use the function "right-strip" rstrip() or "left-strip" lstrip()

favourite_language = 'Python '
print(favourite_language)
favourite_language.rstrip()
print(favourite_language)
