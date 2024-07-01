class ParentClass:
    def parent_method(self):
        print("This is parent method 1.")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Nirupam 2")
        super().parent_method()
    def child_method(self):
        print("This is child method 2.")
        super().parent_method()

child_object = ChildClass()
child_object.child_method()
child_object.parent_method()
