class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal")

class cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="cat")
        self.breed = breed

    def make_sound(self):
        print("Meow!!!")

c = cat("Spider","Persian")
c.make_sound()

a =Animal("Dog","German Shephard")
a.make_sound()