class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and is {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    
    def describe(self):
        print(f"The area of the circle is {3.14159 * self.radius * self.radius:.2f}cm^2")
        super().describe()
    
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    
    def describe(self):
        print(f"The area of the square is {self.width * self.width}cm^2")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    
    def describe(self):
        print(f"The area of the triangle is {0.5 * self.width * self.height}cm^2")
        super().describe()

circle = Circle("Red", True, 5)
square = Square("Blue", False, 2)
triangle = Triangle("Black", False, 5, 4)

print(circle.color)
print(square.width)
print(triangle.is_filled)

print(circle.describe())
print(square.describe())
print(triangle.describe())

