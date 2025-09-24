import json
import csv

textData = "I like movies"

filePath = "UsingFiles/output.txt"

with open(filePath, "w") as file: # write to file
    file.write(textData) # this has to be a string, so if you want to for example write every element in a list, you need to iterate over it (unlike a print statement where you can simply type print(collection))
    print(f"txt file {filePath} was created")

try:
    with open(filePath, "x") as file: # create a file if it doesn't already exist
        file.write(textData)
        print(f"txt file {filePath} was created")
except FileExistsError:
    print("This file already exists")

with open(filePath, "a") as file: # "a" appends text to a file that already exists
    file.write("\n" + textData)

employee = {"name" : "Patrick",
            "age" : "30",
            "job" : "janitor"}

filePath2 = "UsingFiles/output2.json"

with open(filePath2, "w") as file:
    json.dump(employee, file, indent=4) # json files are great for storing key-value type objects
    print(f"json file was created at '{filePath2}'")

employees = [["Name", "Age", "Job"],
             ["Patrick", "30", "janitor"],
             ["John", "31", "Receptionist"],
             ["Caitlin", "21", "Receptionist"]]

filePath3 = "UsingFiles/output3.csv"

with open(filePath3, "w", newline="") as file: # newline="" makes the open method itself not write new lines every time it writes something new (here the writer.writerow method already adds a new line, so we do this to not have an empty row in between)
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"csv file was created at '{filePath3}'")
