
#importar calculos de area y volumen
from utils.caculos_area import *
from utils.calculos_volumen import *

# importar los menus
from utils.menus import *

def main():
    while True:
        menu()
        opcion = input("Selecciona una opcion")
        if opcion == '1':
            while True:
                sub_menu_area()
                figura = input('Selecciona una opcion: ')

                if figura == '0':
                    break

                elif figura == '1': # Area de un cuadrado
                    lado = float(input("Ingrese el lado del cuadrado: "))

                    print('Area del cuadrado:', area_cuadrado(lado))

                elif figura == '2':  # Área del triángulo
                    base = float(input("Ingrese la base del triángulo: "))
                    altura = float(input("Ingrese la altura del triángulo: "))

                    print("Área del triángulo: ", area_triangulo(base, altura))

                elif figura == '3':  # Área del rectangulo
                    longitud = float(input("Ingrese la longitud del rectangulo: "))
                    ancho = float(input("Ingrese el acho del rectangulo: "))

                    print("Área del rectangulo: ", area_rectangulo(longitud, ancho))
                
                elif figura == '4': # Area de un circulo
                    radio = float(input("Ingrese el radio del circulo: "))

                    print('Area del circulo:', area_circulo(radio))
                
                elif figura == '5': # Area de una esfera
                    radio = float(input("Ingrese el radio de la esfera: "))

                    print('Area de la esfera:', area_esfera(radio))
                
                elif figura == '6': # Area de un cilindro
                    radio = float(input("Ingrese el radio del cilindro: "))
                    altura = float(input("Ingrese la altura del cilindro: "))

                    print('Area del cilindro: ', area_cilindro(radio, altura))
                
                elif figura == '7': # Area de una piramide
                    ancho = float(input("Ingrese el ancho de la piramide: "))
                    longitud = float(input("Ingrese la longitud de la piramide: "))
                    altura = float(input("Ingrese la altura de la piramide: "))

                    print('Area del la piramide: ', area_piramide(ancho, longitud, altura))
                
                elif figura == '8': # Area de un prisma
                    ancho = float(input("Ingrese el ancho del prisma: "))
                    longitud = float(input("Ingrese la longitud del prisma: "))
                    altura = float(input("Ingrese la altura del prisma: "))

                    print('Area del prisma: ', area_prisma_rectangular(ancho, longitud, altura))
                
                else:
                    print("Opcion invalida intente de nevo ...")
        
        elif opcion == '2':
            while True:
                sub_menu_volumen()
                figura = input("Seleccione una figura: ")

                if figura == '0':
                    break

                elif figura == '1':  # Volumen del cubo
                    lado = float(input("Ingrese el lado del cubo: "))
                    print("Volumen del cubo:", volumen_cubo(lado))

                elif figura == '2': # Volumen de un cilindro
                    ancho = float(input("Ingrese el ancho del cilindro: "))
                    altura = float(input("Ingrese la altura del cilindro: "))

                    print("Volumen del cilindro: ", voluen_cilindro(ancho, altura))

                elif figura == '3': # Volumen de una piramide
                    ancho = float(input("Ingrese el ancho de la piramide: "))
                    longitud = float(input("Ingrese la longitud de la piramide: "))
                    altura = float(input("Ingrese la altura de la piramide: "))

                    print("Volumen de la piramide: ", volumen_piramide(ancho,longitud,altura))

                elif figura == '4': # Volumen de un prisma
                    ancho = float(input("Ingrese el ancho del prisma: "))
                    longitud = float(input("Ingrese la longitud del prisma: "))
                    altura = float(input("Ingrese la altura del prisma: "))

                    print("Volumen del prisma: ", volumen_piramide(ancho,longitud,altura))

                elif figura == '5': # Volumen de una esfera
                    lado = float(input("Ingrese el radio de la esfera: "))
                    print("Volumen de la esfera:", volumen_esfera(radio))

                elif figura == '6': # Voumen de un cono
                    radio = float(input("Ingrese el radio del cono: "))
                    altura = float(input("Ingrese la altura del cono: "))

                    print("Volumen del cilindro: ", volumen_cono(radio, altura))

                

        elif opcion == '3':
            print("Gracias por usar el programa. ¡Adiós!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")
        
if __name__ == "__main__":
    main()