# 2. Area of Circle by OOPS
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

# Test the class
c = Circle(5)
print(f"Area of circle with radius 5: {c.area()}")