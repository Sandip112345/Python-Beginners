class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")
    def showinstance(self):
        print(f"The instance value of a is {self.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



e = Employee()
e.a = 45
e.show()
e.showinstance() 


e.name = "Sandip Budha"
print(e.name)
print(e.fname)
