class Employee:
    a = 6

class Programmer(Employee):
    b = 9

class Manager(Programmer):
    c = 3

d = Employee()

print(d.a)
# print(d.d.b)

e = Manager()
print(e.b)
print(e.a)

