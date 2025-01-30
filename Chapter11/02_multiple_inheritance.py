class Employee:
    company = "ICT"
    name = "Default"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.company}")

    
class Coder:
    language = "python"
    def printLanguages(self):
        print(f"OUt of all the languages her eis your language {self.language}")


class Programmer(Employee, Coder):
    company = "ICT Infotech"
    def showLanguages(self):
        print(f"The name is {self.company} and he is good with {self.language} language")
        


a = Employee()
b = Programmer()

# print(a.company, b.company)
b.show()
b.printLanguages()
b.showLanguages()


