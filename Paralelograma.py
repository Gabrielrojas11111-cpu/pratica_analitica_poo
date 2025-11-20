from Figurasgeometricas import Figurasgeometricas
from math import pi

class Paralelograma(Figurasgeometricas):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def base(self) -> float:
      return self._base
    
    @base.setter
    def base(self, base: float):
       self._base = base

    @property
    def altura(self)->float:
       return self._altura
    
    @altura.setter
    def altura(self,altura:float):
       self._altura=altura

    def area(self):
       return 2 * pi * self.base * (self.base * self.altura)