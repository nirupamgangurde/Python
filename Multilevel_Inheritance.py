class Cars:
    def __init__(self, Sportscar, hypercar):
        self.Sportscar = Sportscar
        self.hypercar = hypercar

    def new_Brand(self):
        print("Speed 300 Plus")

class pagani(Cars):
    def __init__(self, Sportscar, hyperbike):
        Cars.__init__(self, Sportscar, hypercar="Koenigsegg")
        self.hyperbike = hyperbike
    def new_Brand(self):
        print("Koenigsegg Jesko")

a = pagani("Nano", "Bugatti")
a.new_Brand()

a1 = Cars("ferrari", "GTR")
a1.new_Brand()

class Lambo(pagani):
    def __init__(self, Sportscar, Commuterbike):
        pagani.__init__(self,Sportscar, hyperbike="BMW")
        self.Commuterbike = Commuterbike

    def new_Brand(self):
        print("This is BMW S1000RR")

a3 = Lambo("Mercedes","Hero Splendor")
a3.new_Brand()
