# 5. Multiple Inheritance
class A:
    def feature1(self):
        print("Feature 1 from class A")

class B:
    def feature2(self):
        print("Feature 2 from class B")

class C(A, B):
    def feature3(self):
        print("Feature 3 from class C")

# Test multiple inheritance
obj = C()
obj.feature1()
obj.feature2()
obj.feature3()