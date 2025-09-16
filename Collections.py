# List [] ordered, changeable. Duplicates OK
# Set {} unordered, not changeable (can add or remove elements). NO Duplicates 
# Tuple () ordered and unchangeable, Duplicates OK (basically an array)

fruits = ["apple", "banana", "orange"]

#Python's .add
#fruits.append("pineapple")

fruits.insert(1, "pineapple")

# ,end="" means print in the same line (because it defaults to ending with \n)
print("apple" in fruits, end="")

print(fruits)

fastFoods = {"pizza", "burger", "fries"}

fastFoods.add("nuggets")
fastFoods.remove("pizza")

print(len(fastFoods))
print(fastFoods)

# You initialize 2D collections by simply adding other collections to them
vegetables = ["carrot", "squash", "pepper"]

foods = [vegetables, fruits]

print(foods)
print(foods[0][2])