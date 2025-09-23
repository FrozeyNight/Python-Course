class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, newWidth):
        if(newWidth > 0):
            self._width = newWidth
        else:
            print("Width can't be lower than zero")
    
    @height.setter
    def height(self, newHeight):
        if(newHeight > 0):
            self._height = newHeight
        else:
            print("Height can't be lower than zero")
    
    @width.deleter
    def width(self):
        del self._width
        print("width was deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height was deleted")

rectangle = Rectangle(3, 4)

print(rectangle.width)
print(rectangle.height)

rectangle.width = 2
rectangle.height = 5
rectangle.height = -1

print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)
