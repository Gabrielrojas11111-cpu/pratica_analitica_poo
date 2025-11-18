from Figurasgeometricas import Figurasgeometricas




class Cuadradro(Figurasgeometricas):
    def __init__(self,lado):
        self.lado=lado
    def area(self):
      return self.lado*self.lado