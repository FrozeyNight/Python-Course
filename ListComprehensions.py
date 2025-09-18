# List comprehensions are a faster way to create lists in Python

doubles = [x * 2 for x in range(1,11)]
print(doubles)

fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)

numbers = [1, -2, 3, -4, 5, -6]
positiveNumbers = [num for num in numbers if num >= 0]
print(positiveNumbers)