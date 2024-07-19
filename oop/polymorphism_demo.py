import math

# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(self):
        return  (self.length * self.width)

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2