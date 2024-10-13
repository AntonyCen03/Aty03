class Vehiculo:
    def __init__(self, marca, modelo,color,años,tipo_vehiculo):
        self.marca = marca
        self.modelo = modelo
        self.color=color
        self.años=años
        self.tipo_vehiculo=tipo_vehiculo

class Carro(Vehiculo):
    def __init__(self, marca, modelo,color,años,tipo_vehiculo):
        super().__init__(marca, modelo,color,años,tipo_vehiculo)
    def __str__(self) -> str:
        return(f"""
Tipo de Vehiculo: {self.tipo_vehiculo}
Marca: {self.marca}
Modelo: {self.modelo} 
Color: {self.color}
Años: {self.años}
""")

class Barco(Vehiculo):
    def __init__(self, marca, modelo,color,años,tipo_vehiculo):
        super().__init__(marca, modelo,color,años,tipo_vehiculo)
    
    def __str__(self) -> str:
        return(f"""
Tipo de Vehiculo: {self.tipo_vehiculo}
Marca: {self.marca}
Modelo: {self.modelo} 
Color: {self.color}
Años: {self.años}
""")

class Avion(Vehiculo):
    def __init__(self,marca, modelo,color,años,tipo_vehiculo):
        super().__init__(marca, modelo,color,años,tipo_vehiculo)

    def __str__(self) -> str:
        return(f"""
Tipo de Vehiculo: {self.tipo_vehiculo}
Marca: {self.marca}
Modelo: {self.modelo} 
Color: {self.color}
Años: {self.años}
""")
    
def main():
    carro1=Carro("Toyota","corolla","rojo","2020","Carro")
    print(carro1)
    carro2=Carro("Cherry","Carmy","Azul","2019","Carro")
    print(carro2)
    barco1=Barco("BALI","Pequeños","Blanco","2019","Barco")
    print(barco1)
    barco2=Barco("BALI","Grande","Rojo","2024","Barco")
    print(barco2)
    avion1=Avion("Airbus","A380","Blanco","2018","Avion")
    print(avion1)
    avion2=Avion("Boeing","747","Blanco","2018","Avion")
    print(avion2)

if __name__=="__main__":
    main()

# Función para registrar un vehículo
def registrar_vehiculo(vehiculo):
    print(f"Registrando vehículo: {vehiculo.marca} {vehiculo.modelo} {vehiculo.color} {vehiculo.años} {vehiculo.tipo_vehiculo}")

# Menú de opciones
def mostrar_menu():
    print("Seleccione el tipo de vehículo que desea registrar:")
    print("1. Carro")
    print("2. Barco")
    print("3. Avión")
    print("Marca 'x' para salir ")

mostrar_menu()
while True:
    opcion = input("Ingrese el número de opción: ")

    if opcion=="x":
        break
    if opcion == "1":
        carro = Carro(input("Marca: "),input("Modelo: "),input("Color: "),input("Años: "),input("Tipo de Vehiculo: "))
        registrar_vehiculo(carro)
        print(carro)
    elif opcion == "2":
        barco = Barco(input("Marca: "),input("Modelo: "),input("Color: "),input("Años: "),input("Tipo de Vehiculo: "))
        registrar_vehiculo(barco)
        print(barco)
    elif opcion == "3":
        avion = Avion(input("Marca: "),input("Modelo: "),input("Color: "),input("Años: "),input("Tipo de Vehiculo: "))
        registrar_vehiculo(avion)
        print(avion)
    else:
        print("Opción inválida.")
