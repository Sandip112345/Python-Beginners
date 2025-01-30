class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 6

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 9

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

# d = Employee()

# print(d.a)
# print(d.d.b)

# e = Manager()
# print(e.b)
# print(e.a)

# o = Programmer()
o = Manager()

