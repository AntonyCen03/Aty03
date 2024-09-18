print("Bienvenido al mundo pokermon")

genero=(str(input("Eres niños o niñas: ")))

if genero == "niños":
    print("Bienvenido")
else:
    if genero == "niñas":
        print("Bienvenida")
    else:
        print("Debe ingresar niñas o niños")
    
edad=int(input("Cuanto años tiene: "))
if int(edad)<10:
    if genero == "niños":
        print("no tiene edad para ser entrenador")
    else:
         print("no tiene edad para ser entrenadora")
         quit()

print("Comineza tu aventura")

print("""lista de region
         1. Kanto""")
region = str(input("Necesita un compañero de viaje. en que region se encuentra: "))
        
if region == "Kanto" and genero == "niños":
     print("tu compañero de viaje es Misty")
else:
     print("tu compañera de viaje es Brook")


print("""-------lista de pokemon------
 1. Agua
 2. Fuego
 3. Planta   """)   
 
tipo =input("Ingrese el tipo de pokermon para empezar: ")

if tipo == "Agua" or "1":
    print("tu starter es 123")
elif tipo == "Fuego" or "2":
    print("tu starter es 456")
elif tipo == "Planta" or "3" :
    print("tu starter es 789")
else:
    print("""no tengo ese tipo.
             Seleciona de nuevo""")

input("Dale cualquier tecla para salirse!")
