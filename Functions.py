def fullName(firstName, lastName):
    return firstName.capitalize() + " " + lastName.capitalize()

def displayName(fullName):
    print(f"Hello, {fullName}!")
    print("Welcome to our website!")

displayName(fullName("steve", "fireheart"))
displayName(fullName("joe", "napkins"))
displayName(fullName("diana", "fishbang"))

# default arguments are parameters that have a default value if they are not passed
def netPrice(price, discount = 0, tax = 0.05):
    return price * (1 - discount) * (1 + tax)

print(netPrice(500))
print(netPrice(500, 0.1))
print(netPrice(500, 0.2, 0))

# keyword arguments make it so the order in which you pass arguments doesn't matter
def welcome(greeting, title, firstName, lastName):
    print(f"{greeting} {title}{firstName} {lastName}")

welcome(lastName="Jobs", greeting="Hello", title="Mr.", firstName="Joe")
# an example of when it's good to use keyword arguments (it makes it easier to read which is which, especially helpful with if you pass a lot of numbers)
welcome("Hi", "Mr.", firstName="James", lastName="John")

# *args allows you to make the function take any amount of arguments (*args is a tuple)

def showName(*args):
    for arg in args:
        print(arg, end=" ")
    print()

showName("Adam", "Smith")
showName("Dr.", "Carl", "Harold", "Musk", "III")

# *kwargs is the same thing as args, but you can pass in any amount of keyword arguments (**kwargs is a dictionary)
def displayAddress(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

displayAddress(street="Fake st. 253", city="Detroit", state="MI")
displayAddress(street="Fake st. 123", apt="61", city="Cleveland", state="Ohio", zip="12345")

def shippingLabel(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    #for value in kwargs.values():
    #    print(value, end=" ")
    #print()
    if "apt" in kwargs:
        # here we need to use ' instead of " inside of the .get method, since otherwise Python will thing we are ending the whole string there
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shippingLabel("Dr.", "Carl", "Harold", "Musk", "III", street="Fake st. 123", apt="61", city="Cleveland", state="Ohio", zip="12345")
shippingLabel("Adam", "Smith", street="Fake st. 253", city="Detroit", state="MI", zip="12345")