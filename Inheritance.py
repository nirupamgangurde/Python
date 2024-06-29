class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"Name of Employee is : {self.id} is {self.name}")

class Programmer(Employee):
    def Showlanguage(self):
        print("The default language is python")

e1 = Employee("Rohan", 400)
e1.showDetails()
e2 = Programmer("Nishad",401)
e2.showDetails()
e2.Showlanguage()