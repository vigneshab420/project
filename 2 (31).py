# 4. Inheritance Example
class Animal:
    def speak(self):
        print("Animal speaking")

class Dog(Animal):
    def speak(self):
        print("Dog is barking")

class Cat(Animal):
    def speak(self):
        print("Cat is meowing")

# Test inheritance
d = Dog()
c = Cat()
d.speak()
c.speak()