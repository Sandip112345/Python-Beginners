class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
    def showinstance(self):
        print(f"The instance value of a is {self.a}")


e = Employee()
e.a = 45

e.show()
e.showinstance()