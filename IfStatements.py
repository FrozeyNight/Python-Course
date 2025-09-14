
#age = int(input("What is your age?: "))
age = 25

#if 100 > age >= 18:
if age >= 18 and age < 100:
    print("You can use this program!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You are too old for this!")

is_Sunny = True
is_Cold = False

if is_Sunny and not is_Cold:
    print("We can go out today!")
elif is_Sunny and is_Cold:
    print("It's sunny, but it's too cold!")
else:
    print("The weather is just not ideal for a hang out!")

num = 1

result =  "Even" if num % 2 == 0 else "Odd"
print(result)

x = 6
y = 18

max = x if x > y else y
print(max)