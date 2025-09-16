num = int(input("Please enter a whole number between 1 and 10: "))

while num < 1 or num > 10:
    print(f"{num} is not in the range!")
    num = int(input("Please enter a whole number between 1 and 10: "))

print(f"You picked {num}!")

for x in range(1, 6):
    print(x)

for x in reversed(range(1, 6)):
    print(x)

# the third parameter is step, the same as in string indexes. 
for x in range(1, 11, 2):
    print(x)

credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

# continue and break keywords work the same as in other programming languages