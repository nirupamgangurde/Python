class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name= name

D = DancerEmployee("Kathak","Shivani")
print(D.name)
print(D.dance)
D.show() #Here if we chance parameters from Employee, Dancer (line number 14) to Dancer, Employee then Output will be : the dance is kathak