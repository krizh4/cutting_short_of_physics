#classes:kinetic class
class E_k:
    def __init__(self, mass, velocity):
        self.m = mass
        self.v = velocity
    
    def answer_kinetic(self):
        x = 1 / 2 * float(self.m) * float(self.v) ** 2
        print(f"{x} J")
