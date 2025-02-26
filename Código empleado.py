import json

class Empleado:
    """Clase que representa a un empleado."""
    
    def __init__(self, nombre: str, edad: int, cargo: str, salario_base: float):
        """Inicializa un empleado con su nombre, edad, cargo y salario base."""
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.salario_base = salario_base
        self.salario_total = self.calcular_salario()

    def calcular_salario(self) -> float:
        """Calcula el salario total basado en el cargo del empleado."""
        bonificaciones = {"Gerente": 500, "Desarrollador": 300, "Diseñador": 200}
        return self.salario_base + bonificaciones.get(self.cargo, 0)

    def mostrar_informacion(self) -> str:
        """Retorna la información del empleado en formato de cadena."""
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Cargo: {self.cargo}, Salario: {self.salario_total}"


class SistemaEmpleados:
    """Clase que maneja el sistema de gestión de empleados."""
    
    def __init__(self):
        """Inicializa un sistema sin empleados."""
        self.empleados = []

    def agregar_empleado(self):
        """Solicita información al usuario y agrega un nuevo empleado."""
        nombre = input("Nombre del empleado: ")
        edad = int(input("Edad: "))
        cargo = input("Cargo (Gerente, Desarrollador, Diseñador): ")
        salario_base = float(input("Salario base: "))
        self.empleados.append(Empleado(nombre, edad, cargo, salario_base))

    def mostrar_empleados(self):
        """Muestra la lista de empleados registrados."""
        if not self.empleados:
            print("No hay empleados registrados.")
        for empleado in self.empleados:
            print(empleado.mostrar_informacion())

    def calcular_salario(self):
        """Busca un empleado por su nombre y muestra su salario total."""
        nombre_buscar = input("Ingrese el nombre del empleado: ")
        for empleado in self.empleados:
            if empleado.nombre == nombre_buscar:
                print(f"El salario de {nombre_buscar} es: {empleado.salario_total}")
                return
        print("Empleado no encontrado.")

    def buscar_empleado_por_cargo(self):
        """Busca empleados por su cargo y muestra su información."""
        cargo_buscar = input("Ingrese el cargo a buscar: ")
        encontrados = [empleado for empleado in self.empleados if empleado.cargo == cargo_buscar]
        if encontrados:
            for empleado in encontrados:
                print(empleado.mostrar_informacion())
        else:
            print("No se encontraron empleados con ese cargo.")

    def eliminar_empleado(self):
        """Elimina un empleado por su nombre."""
        nombre_eliminar = input("Ingrese el nombre del empleado a eliminar: ")
        for empleado in self.empleados:
            if empleado.nombre == nombre_eliminar:
                self.empleados.remove(empleado)
                print(f"Empleado {nombre_eliminar} eliminado.")
                return
        print("Empleado no encontrado.")

    def actualizar_empleado(self):
        """Actualiza la información de un empleado."""
        nombre_actualizar = input("Ingrese el nombre del empleado a actualizar: ")
        for empleado in self.empleados:
            if empleado.nombre == nombre_actualizar:
                nuevo_nombre = input("Nuevo nombre (dejar en blanco para no cambiar): ")
                nueva_edad = input("Nueva edad (dejar en blanco para no cambiar): ")
                nuevo_cargo = input("Nuevo cargo (dejar en blanco para no cambiar): ")
                nuevo_salario_base = input("Nuevo salario base (dejar en blanco para no cambiar): ")
                
                if nuevo_nombre:
                    empleado.nombre = nuevo_nombre
                if nueva_edad:
                    empleado.edad = int(nueva_edad)
                if nuevo_cargo:
                    empleado.cargo = nuevo_cargo
                if nuevo_salario_base:
                    empleado.salario_base = float(nuevo_salario_base)
                
                empleado.salario_total = empleado.calcular_salario()
                print(f"Empleado {nombre_actualizar} actualizado.")
                return
        print("Empleado no encontrado.")

    def guardar_empleados(self):
        """Guarda la lista de empleados en un archivo JSON."""
        with open("empleados.json", "w") as archivo:
            json.dump([empleado.__dict__ for empleado in self.empleados], archivo)
        print("Empleados guardados en empleados.json")

    def cargar_empleados(self):
        """Carga la lista de empleados desde un archivo JSON."""
        try:
            with open("empleados.json", "r") as archivo:
                empleados_data = json.load(archivo)
                self.empleados = [Empleado(**data) for data in empleados_data]
            print("Empleados cargados desde empleados.json")
        except FileNotFoundError:
            print("Archivo empleados.json no encontrado.")

    def menu(self):
        """Muestra el menú interactivo del sistema de empleados."""
        opcion = 0
        while opcion != 9:
            print("\n1. Agregar empleado\n2. Mostrar empleados\n3. Calcular salario\n4. Buscar empleado por cargo\n5. Eliminar empleado\n6. Actualizar empleado\n7. Guardar empleados\n8. Cargar empleados\n9. Salir")
            try:
                opcion = int(input("Elige una opción: "))
                if opcion == 1:
                    self.agregar_empleado()
                elif opcion == 2:
                    self.mostrar_empleados()
                elif opcion == 3:
                    self.calcular_salario()
                elif opcion == 4:
                    self.buscar_empleado_por_cargo()
                elif opcion == 5:
                    self.eliminar_empleado()
                elif opcion == 6:
                    self.actualizar_empleado()
                elif opcion == 7:
                    self.guardar_empleados()
                elif opcion == 8:
                    self.cargar_empleados()
                elif opcion == 9:
                    print("Saliendo...")
                else:
                    print("Opción no válida")
            except ValueError:
                print("Error: Ingrese un número válido.")


class T9Converter:
    """Clase para convertir pulsaciones T9 a texto."""
    
    def __init__(self):
        """Inicializa el diccionario de conversión de T9."""
        self.t9_dict = {
            "2": "A", "22": "B", "222": "C", "3": "D", "33": "E", "333": "F",
            "4": "G", "44": "H", "444": "I", "5": "J", "55": "K", "555": "L",
            "6": "M", "66": "N", "666": "O", "7": "P", "77": "Q", "777": "R", "7777": "S",
            "8": "T", "88": "U", "888": "V", "9": "W", "99": "X", "999": "Y", "9999": "Z"
        }
    
    def t9_a_texto(self, codigo_t9: str) -> str:
        """Convierte una cadena de pulsaciones T9 en texto."""
        bloques = codigo_t9.split("-")
        texto = "".join(self.t9_dict.get(bloque, "") for bloque in bloques)
        return texto

    def texto_a_t9(self, texto: str) -> str:
        """Convierte una cadena de texto en pulsaciones T9."""
        texto = texto.upper()
        inverso_t9_dict = {v: k for k, v in self.t9_dict.items()}
        codigo_t9 = "-".join(inverso_t9_dict.get(char, "") for char in texto)
        return codigo_t9


if __name__ == "__main__":
    sistema = SistemaEmpleados()
    sistema.menu()
    
    # Ejemplo de uso del conversor T9
    entrada_t9 = "6-666-88-777-33-3-33-888"
    converter = T9Converter()
    print("Salida:", converter.t9_a_texto(entrada_t9))
    # Ejemplo de conversión de texto a T9
    texto = "MUNDO"
    print("T9:", converter.texto_a_t9(texto))