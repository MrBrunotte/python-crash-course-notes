# 8.1 - Message
excercise = "8.1 - Message"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def display_message():
    """A function that prints what I am learning in this chapter"""
    print("In this chapter we learn about functions!")


display_message()

# 8.2 - Favorite Book
excercise = "8.2 - Favorite Book"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def favorite_book(title):
    """ Write a function that accepts one PARAMETER 'title'
        Call the function and include a book title as an ARGUMENT
    """
    print(f"One of my favorite books are {title.title()}!")


favorite_book('bilbo')


# 8.3 - T-Shirt
excercise = "8.3 - T-Shirt"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def make_shirt(size, text):
    """
    A function that has two PARAMETER 'size and text'
    When the arguments are passed in the size and text will be printed
    """
    print(
        f"The size of your T-Shirt is: {size.upper()}\nThe text will be: '{text.upper()}'\n")


# positional agruments
make_shirt('l', 'This is my T-Shrit')
# Keyword agruments
make_shirt(size='l', text='This is my T-Shrit')

# 8.4 - Large Shirts
excercise = "8.4 - Large Shirts"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def make_shirt(text, size='Large'):
    """
    Size has L as default value
    """
    print(
        f"The size of your T-Shirt is: {size.upper()}\nThe text will be: '{text.upper()}'\n")


make_shirt('I love Python')

# 8.5 - Cities
excercise = "8.5 - Cities"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def describe_city(city, country='sweden'):
    """ DOCSTRING"""
    print(f"{city.title()} is a city in {country.upper()}.")


describe_city('stockholm')
describe_city('göteborg')
# overwrite the default paramater='Sweden'
describe_city('New york', country='USA')

# 8.6 - City Names
excercise = "8.6 - City Names"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def city_country(city_name, country):
    ''' Function that should return a value like this: Stockholm, Sweden '''
    name_country = f"{city_name}, {country}"
    return name_country.title()


city_country_pair = city_country('stockholm', 'sweden')
print(city_country_pair)

# 8.7 - Album
excercise = "8.7 - Album"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


# def make_album(artist_name, album_title):
#     ''' A function that returns Bob Marley, Legend '''
#     album = {
#         'artist': artist_name,
#         'album': album_title,
#     }
#     return album


# artist_album = make_album('bob marley', 'legend')
# print(artist_album)
# artist_album = make_album('peter tosh', 'legalize it')
# print(artist_album)
# artist_album = make_album('mixed songs', 'chill music')
# print(artist_album)

# print('\n')

# # add OPTIONAL parameter


# def make_album(artist_name, album_title, tracks=None):
#     ''' A function that returns An artist name, album title and number of songs if it is added!'''
#     album = {
#         'artist': artist_name,
#         'album': album_title,
#     }

#     if tracks:
#         album['tracks'] = tracks
#     return album


# artist_album = make_album('bob marley', 'legend', 25)
# print(artist_album)
# artist_album = make_album('peter tosh', 'legalize it', 10)
# print(artist_album)
# artist_album = make_album('mixed songs', 'chill music')
# print(artist_album)

# 8.8 - User Albums
excercise = "8.8 - User Albums"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


# def make_album(artist_name, album_title, tracks=None):
#     ''' A function that returns An artist name, album title and number of songs if it is added!
#         A while loop is added to let the user add artists, titles and number of songs'''
#     album_dict = {
#         'artist': artist_name.title(),
#         'album': album_title.title(),
#     }
#     if tracks:
#         album_dict['tracks'] = tracks
#     return album_dict


# # prepare the prompts
# artist_prompt = "\nWho's the artist?\t\t "
# title_prompt = "What album are you thinking of?\t "
# tracks_prompt = "\n(Leave empty if you don't know)\nHow many tracks on the album?\t "
# end_prompt = "\nDo you want to add another artist and album? (y/n) "

# # Let the user know how to quit
# print("Enter 'q' at any time to stop.")


# while True:
#     artist = input(artist_prompt)
#     if artist == 'q':
#         break

#     title = input(title_prompt)
#     if title == 'q':
#         break

#     tracks = input(tracks_prompt)
#     if title == 'q':
#         break

#     album = make_album(artist, title, tracks)
#     print(album)

#     end = input(end_prompt)
#     if end == 'n':
#         print("\nGood Bye! Thanks for your input!")
#         break

# 8.9 - Messages
excercise = "8.9 - Messages"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def show_messages(messages):
    for message in messages:
        print(message.title())


messages = ['I like playing golf', 'I also like tennis',
            'I also like playing paddle', 'I like squash']
show_messages(messages)

# 8.10 - Sending Messages
excercise = "8.10 - Sending Messages"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def show_messages(messages):
    ''' Print all messages in the list '''
    print("Show all messages:")
    print(messages)
    print("\n")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    ''' printing each message, and then move it to sent_messages '''
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

#------------ funcitons end -------------#


messages = ['I like playing golf', 'I also like tennis',
            'I also like playing paddle', 'I like squash']
show_messages(messages)


sent_messages = []

print("\nOrignal lists:")
print("Messages list:")
print(messages)
print("Sent messages list:")
print(sent_messages)

send_messages(messages, sent_messages)

print("\nFinal lists:")
print("Messages list:")
print(messages)
print("Sent messages list:")
print(sent_messages)

# 8.11 - Archived Messages
excercise = "8.11 - Archived Messages"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def show_messages(messages):
    ''' Print all messages in the list '''
    print("Show all messages:")
    print(messages)
    print("\n")
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    ''' printing each message, and then move it to sent_messages '''
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

#------------ funcitons end -------------#


messages = ['I like playing golf', 'I also like tennis',
            'I also like playing paddle', 'I like squash']
# messages is the ARGUMENT
show_messages(messages)

sent_messages = []
# copy the original messages list!
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)

# 8.12 - Sandwiches
excercise = "8.12 - Sandwiches"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def sandwiches(*toppings):
    ''' create a function the takes any number or arguments with the *args parameter '''
    print(f"\nThese are the toppings on your sandwich:")
    for topping in toppings:
        print(f"- {topping.title()}.")


sandwiches('ham', 'turkey', 'jalapenos', 'cheese', 'lettuce', 'tomatos')
sandwiches('lettuce', 'tomatos')
sandwiches('ham', 'turkey', 'jalapenos')

# 8.13 - User Profile
excercise = "8.13 - User Profile"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def build_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user'''
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    return user_info


user_profile = build_profile(
    'stefan',
    'brunotte',
    location='stockholm',
    field='coding',
    age='48',
    number_of_children='1',
)

print(user_profile)

# 8.14 - Cars
excercise = "8.14 - Cars"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")


def car(make, model, **car_info):
    ''' A function that recieves two positional args and arbitrary keyword arguments **kwargs '''
    car_dict = {
        'make': make.title(),
        'model': model.title(),
    }
    for info, value in car_info.items():
        car_dict[info] = value

    return car_dict


my_car = car(
    'ferrari',
    'f500',
    color='red'.title(),
    top_speed='350',
    cost='3 500 555'
)
my_old_car = car(
    'lambourghini',
    'spider',
    color='black'.title(),
    top_speed='360',
    cost='3 000 555'
)

print("My old car dictionary:")
print(my_old_car)
print("\nMy new car dictionary:")
print(my_car)

# 8.15 - Printing Models
excercise = "8.15 - Printing Models"
print("\n#--------------------------------------------------#")
print("\t" + excercise.upper() + "\t")
print("#--------------------------------------------------#\n")
