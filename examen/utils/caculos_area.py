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

class Cuadrado(Figura):
    def __init__(self, lado, color="blanco"):
        super().__init__("Cuadrado", color)
        self._lado = lado
    
    def calcular_area(self):
        return self._lado ** 2
    
    def calcular_perimetro(self):
        return 4 * self._lado

class Triangulo(Figura):
    def __init__(self, base, altura, lado1, lado2, lado3, color="blanco"):
        super().__init__("Triángulo", color)
        self._base = base
        self._altura = altura
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3
    
    def calcular_area(self):
        return 0.5 * self._base * self._altura
    
    def calcular_perimetro(self):
        return self._lado1 + self._lado2 + self._lado3

class Circulo(Figura):
    def __init__(self, radio, color="blanco"):
        super().__init__("Círculo", color)
        self._radio = radio
    
    def calcular_area(self):
        return np.pi * self._radio ** 2
    
    def calcular_perimetro(self):
        return 2 * np.pi * self._radio

def main():
    while True:
        print("Seleccione una figura geométrica:")
        print("1. Cuadrado")
        print("2. Triángulo")
        print("3. Círculo")
        print("4. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            color = input("Ingrese el color del cuadrado: ")
            cuadrado = Cuadrado(lado, color)
            print(f"Área del {cuadrado._nombre}: {cuadrado.calcular_area()}")
            print(f"Perímetro del {cuadrado._nombre}: {cuadrado.calcular_perimetro()}")

        elif opcion == "2":
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            lado1 = float(input("Ingrese el lado 1 del triángulo: "))
            lado2 = float(input("Ingrese el lado 2 del triángulo: "))
            lado3 = float(input("Ingrese el lado 3 del triángulo: "))
            color = input("Ingrese el color del triángulo: ")
            triangulo = Triangulo(base, altura, lado1, lado2, lado3, color)
            print(f"Área del {triangulo._nombre}: {triangulo.calcular_area()}")
            print(f"Perímetro del {triangulo._nombre}: {triangulo.calcular_perimetro()}")

        elif opcion == "3":
            radio = float(input("Ingrese el radio del círculo: "))
            color = input("Ingrese el color del círculo: ")
            circulo = Circulo(radio, color)
            print(f"Área del {circulo._nombre}: {circulo.calcular_area()}")
            print(f"Perímetro del {circulo._nombre}: {circulo.calcular_perimetro()}")

        elif opcion == "4":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
