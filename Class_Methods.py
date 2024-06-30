class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and comany is {self.company}")
    @classmethod
    def changeCompany(cls, newcompany): #Here cls is nothis but it is self
        cls.company = newcompany

e1 = Employee()
e1.name = "Vaibhav"
e1.show()
e1.changeCompany("Tesla")
e1.show()