Años = int(input("ingresa el años que desea calcular: "))

if Años >= 1900 < 2199:
    Años_f=int(1900)
    Años_bicieto= (Años - Años_f) // 4
    if Años % 4 == 0:
        print(Años,"Es un años bicieto ")
        print(f"lleva {Años_bicieto} años bicieto")    
    else:
        print(Años,"no es un años bicieto ")
        print(f"lleva {Años_bicieto} años bicieto") 
else:
    print("el años debe ser entre 1900-2199")

input("marca cualquier tecla para salir")