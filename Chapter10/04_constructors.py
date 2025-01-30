

class Employee:
    language = "Python" # this is a class attribute
    salary = 145000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        
        print(f"The Language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")



dip = Employee("Dip Budha", 135343, "BashScript")    # Calls the init function
print(dip.name, dip.salary, dip.language)

