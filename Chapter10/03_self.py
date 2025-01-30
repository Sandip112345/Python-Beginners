

class Employee:
    language = "Python"
    salary = 145000

    def getInfo(self):
        print(f"The Language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")

sandy = Employee()
sandy.language = "BashScript"

sandy.getInfo()
sandy.greet()