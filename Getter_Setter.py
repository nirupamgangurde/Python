class Hello:
    def __init__(self,age = 0):
        self._age = age
    def get_age(self):
        return self._age
    def set_age(self, a):
        self._age=a
john = Hello()
john.set_age(18)
print(john.get_age())
print(john._age)