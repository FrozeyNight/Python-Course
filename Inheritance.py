class Animal:
    def __init__(self, name):
        self.name = name
        self.isAlive = True
    
    def eat(self):
        print(f"{self.name} is eating!")
    
    def sleep(self):
        print(f"{self.name} is sleeping!")
    

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeak!")

dog = Dog("Estus")
cat = Cat("Fluff")
mouse = Mouse("Freddy")

dog.eat()
print(cat.isAlive)
mouse.sleep()

dog.speak()
cat.speak()
mouse.speak()