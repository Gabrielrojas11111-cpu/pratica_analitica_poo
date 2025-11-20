from Figurasgeometricas   import Figurasgeometricas
import math

class Esfera(Figurasgeometricas):

    def __init__(self, radio: float, nombre="Esfera"):
        super().__init__(nombre)
        self._radio = radio

 
    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        self._radio = valor

    def area(self):
        return 4 * math.pi * (self.radio ** 2)