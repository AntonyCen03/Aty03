while True:
    Años = input("Ingrese el Años que desea calcular: ").upper()
    if Años == "X":
        break
    if not Años.isnumeric():
        print("Entrada Invalida")
        continue
    Años = int(Años)
    if Años >= 1900 < 2199:
        Años_f=int(1900)
        Años_bicieto= (Años - Años_f) // 4
        if Años % 4 == 0:
            print(Años,"Es un años bicieto ")
            print(f"lleva {Años_bicieto} años bicieto")
            print("Si desea salir marca 'X' ")   
        else:
            print(Años,"no es un años bicieto ")
            print(f"lleva {Años_bicieto} años bicieto")
            print("Si desea salir marca 'X' ") 
    else:
        print("el años debe ser entre 1900-2199")
        print("Si desea salir marca 'X' ")