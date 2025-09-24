import os

filePath = "UsingFiles/test.txt"

if os.path.exists(filePath):
    print(f"The location {filePath} exists")

    if os.path.isfile(filePath):
        print("This is a file")
    elif os.path.isdir(filePath):
        print("This is a folder")
else:
    print(f"The location {filePath} does not exist")



