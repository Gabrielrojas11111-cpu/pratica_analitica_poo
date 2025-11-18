from Figurasgeometricas import Figurasgeometricas

class Circulo(Figurasgeometricas):

    def __init__(self,radio):
        self.radio=radio

    def area(self):
        pi=3.1416
        return pi*self.radio*self.radio

        