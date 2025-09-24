import json
import csv

filePath = "UsingFiles/output.txt"

try:
    with open(filePath, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"{filePath} does not exist")
except PermissionError:
    print(f"You do not have permission to read {filePath}")

filePath2 = "UsingFiles/output2.json"

try:
    with open(filePath2, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print(f"{filePath2} does not exist")
except PermissionError:
    print(f"You do not have permission to read {filePath2}")

filePath3 = "UsingFiles/output3.csv"

try:
    with open(filePath3, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)

        for line2 in content: # this won't display anything because the csv.reader() is not a string, but a reader. Once you iterate through it once, it will be empty
            print(line2[0])
except FileNotFoundError:
    print(f"{filePath3} does not exist")
except PermissionError:
    print(f"You do not have permission to read {filePath3}")