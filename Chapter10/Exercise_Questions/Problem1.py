'''
Create a class program for storing information of few programmers working 
at microsoft.

'''

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):

        self.name = name
        self.salary = salary
        self.pin = pin
p = Programmer("Sandip", 1230000, 232422)
print(p.name, p.salary, p.pin, p.company)
r = Programmer("Programmer", 150000, 234242)
print(r.name, r.salary, r.pin, r.company)