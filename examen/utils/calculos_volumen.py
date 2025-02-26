from abc import ABC, abstractmethod
import numpy as np

class Figura(ABC):
    def __init__(self, nombre, color):
        self._nombre = nombre
        self._color = color
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    @abstractmethod
    def calcular_perimetro(self):
        pass

class FiguraVolumetrica(Figura):
    @abstractmethod
    def calcular_volumen(self):
        pass

class Cubo(FiguraVolumetrica):
    def __init__(self, lado, color="blanco"):
        super().__init__("Cubo", color)
        self.lado = lado
    
    def calcular_area(self):
        return 6 * self.lado ** 2
    
    def calcular_perimetro(self):
        return 12 * self.lado
    
    def calcular_volumen(self):
        return self.lado ** 3

class Cilindro(FiguraVolumetrica):
    def __init__(self, radio, altura, color="blanco"):
        super().__init__("Cilindro", color)
        self.radio = radio
        self.altura = altura
    
    def calcular_area(self):
        return 2 * np.pi * self.radio * (self.radio + self.altura)
    
    def calcular_perimetro(self):
        return 2 * np.pi * self.radio
    
    def calcular_volumen(self):
        return np.pi * self.radio ** 2 * self.altura

class Esfera(FiguraVolumetrica):
    def __init__(self, radio, color="blanco"):
        super().__init__("Esfera", color)
        self.radio = radio
    
    def calcular_area(self):
        return 4 * np.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 0  # No aplica en una esfera
    
    def calcular_volumen(self):
        return (4/3) * np.pi * self.radio ** 3