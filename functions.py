#classes:kinetic class
class E_k:
    def __init__(self, mass, velocity):
        self.m = mass
        self.v = velocity
    
    def answer_kinetic(self):
        x = 1 / 2 * float(self.m) * float(self.v) ** 2
        print(f"{x} J")
#classes:potential energy
class E_p:
    def __init__(self, mass, height, gravity):
        self.m = mass
        self.h = height
        self.g = gravity
    
    def answer_potential(self):
        z = float(self.m) * float(self.h) * float(self.g)
        print(f"{z} J")