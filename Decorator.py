def addSprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add some sprinkles*")
        func(*args, **kwargs)
    return wrapper

def addFudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge*")
        func(*args, **kwargs)
    return wrapper

@addSprinkles
@addFudge
def getIceCream(flavor):
    print(f"Here is your {flavor} ice cream")

getIceCream("Vanilla")