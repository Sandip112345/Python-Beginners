'''
Add a static method in problem 2 to greet 
the user with hello.

'''

class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The sqrt is {self.n**0.5}")
    @staticmethod
    def hello():
        print("Hello There!")


num = Calculator(45)

num.square()
num.cube()
num.squareroot()
num.hello()