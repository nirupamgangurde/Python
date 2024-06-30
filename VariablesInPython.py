class Employee:
    companyName = "Apple" #Class variable
    noofEmployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02 #Instance Veriable
        Employee.noofEmployees += 1
    def showDetails(self):
        print(f"The name of Employee is {self.name} and the raise amount in {self.noofEmployees} sized {self.companyName} is {self.raise_amount}")

emp1 = Employee("Vaibhav")
emp1.companyName = "Microsoft" #Instance Variable
emp1.raise_amount = 0.03
emp1.showDetails()

emp2 = Employee("Amit")
emp2.showDetails()
