# 6. Polymorphism Example
class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Polymorphic behavior
shapes = [Square(4), Circle(5)]
for shape in shapes:
    print(f"Area: {shape.area()}")