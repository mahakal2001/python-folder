'''

class phone():
    def call(self):
        print("You can call")

    def meassage(self):
        print("You can meassage")


class oppo(phone):
    # phone er "call" and "meassage" cola asa6a.

    def photo(self):
        print("You can photo viwe")

s = oppo()
s.call()
s.meassage()
s.photo()
'''

# inheritance:=


class shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("i am area method of shape class")


class triangle(shape):
    def area(self):
        area = 0.5*self.dim1*self.dim2
        print("area of triangle", area)

class rectangle(shape):
    def area(self):
        area = self.dim1*self.dim2
        print("area of rectangle", area)

t=triangle(20, 30)
t.area()

r= rectangle(10,20)
r.area()

# Types of Inheritance :
        # (1) Hierarchical Inheritance.
        # (2) Multi Level Inheritance.
        # (3) Multiple Inheritance.


#(1) Hierarchical Inheritance:=

class A:
    def display1(self):
        print("I am Inside A class")

class B(A):
    def display2(self):
        print("I am Inside B class")

class C(B):
    def display3(self):
        print("I am Inside C class")

num1 = C()
num1.display1()
num1.display2()
num1.display3()

