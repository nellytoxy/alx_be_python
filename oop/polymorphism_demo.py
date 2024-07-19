
import math

# Base class Shape
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Derived class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2