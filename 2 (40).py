# 3. Encapsulation Example
class Data:
    def __init__(self):
        self.name = "Hari"
        self.__private_var = "abc"  # Private variable
    
    def show_private(self):
        print(f"Private variable: {self.__private_var}")

# Create object
obj = Data()
print(f"Public variable: {obj.name}")
obj.show_private()  # Access private variable via method