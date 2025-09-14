import math

first_name = "Frozey"

# The default type of a variable with a decimal point is float, even without adding the f after.
price = 52.60

print(f"Hey, {first_name}")

boolean = True
boolean2 = False

print(type(price))

price = str(price)

print(type(price))

age = int(input("What is your age?: "))
print(f"You are {age} years old!")

x = 4
y = 2
z = 41

print(max(x, y, z))

a = 9.2

print(round(a))
print(math.ceil(a))
print(math.floor(a))

b = 16

print(math.sqrt(b))