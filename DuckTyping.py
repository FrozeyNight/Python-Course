class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car: # Duck typing means that if an object has the same attributes as a different object, you can treat it as that other type of object for the purpose of creating lists and such. 
    alive = False

    def speak(self):
        print("Honk!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    print(animal.speak())
    print(animal.alive)