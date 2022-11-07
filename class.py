class airplane:
    def __init__(self, airtype):
        self.airtype = airtype
        self.cspeed = 0
        self.inair = False
        self.fuel = 5000
        
    def printp(self):
        print("airplane type is", self.airtype)
        print("speed is", self.cspeed)
        if self.inair == False:
            print("Status: on ground")
        else:
            print("Status: In Air")
        print("Fuel is currently at", self.fuel)
        print()
    
    def lift(self):
        print("lift off")
        self.inair = True
        self.cspeed = 400
    def land(self):
        print("landing")
        self.inair = False
        self.cspeed = 0
    
    def fly(self):
        self.fuel -= 1000
        print()

a1 = airplane("boeing 737")
a1.printp()
a2 = airplane("P-40E Warhawk")
a2.printp()
a1.lift()
a1.fly()
a1.printp()
