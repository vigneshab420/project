# 1. OOPS Demo Code
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello my name is {self.name} and I am {self.age} years old")

# Create object and call method
al = A("Alice", 25)
al.greet()