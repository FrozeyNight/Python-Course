from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
    
    def area(self):
        return self.width * self.width

class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return 0.5 * self.width * self.height

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping
    
shapes = [Circle(4), Square(5), Triangle(6,7), Pizza(15, "pepperoni")]

for shape in shapes:
    print(shape.area())
