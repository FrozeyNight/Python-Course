def favoriteFood(food):
    print(f"Your favorite food is {food}!")

def main():
    print("This is the ifName file")
    favoriteFood("sushi")

if __name__ == '__main__': # You will find this in a lot of Python files. It checks if the file is being run as main, and if so, it will run the main(). Otherwise (for example when importing this module in a different file) it won't run the main() and simply give access to all of it's variables and methods.
    main()