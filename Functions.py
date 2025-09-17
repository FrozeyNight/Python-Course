def fullName(firstName, lastName):
    return firstName.capitalize() + " " + lastName.capitalize()

def displayName(fullName):
    print(f"Hello, {fullName}!")
    print("Welcome to our website!")

displayName(fullName("steve", "fireheart"))
displayName(fullName("joe", "napkins"))
displayName(fullName("diana", "fishbang"))

