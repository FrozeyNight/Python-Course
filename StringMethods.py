example = "Black Box"

test = example.capitalize()
print(test)

test = test.lower()
print(test)

test = example
# indexOf and lastIndexOf
print(test.find("B"))
print(test.rfind("B"))

# Checks whether a string contains only digits or only alphabetical characters
print(test.isdigit())
print(test.isalpha())

# Counts how many times a given char is in a string
print(test.count("B"))

# Prints information about a given variable including all methods
#print(help(str))

print("-----------------")

credit_card_example = "1234-5678-9012-3456"

# Indexing [start : end : step] - step means a skip (for example ::2 will give every other character)
print(credit_card_example[0])
print(credit_card_example[0:4])
print(credit_card_example[5:9])
print(credit_card_example[:9])
print(credit_card_example[::2])

# Negative indexes are coming from behind (so -1 would be the last character, -2  second to last and so on)
print(credit_card_example[-1])
print(credit_card_example[::-1]) # this will reverse the string
