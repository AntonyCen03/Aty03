agua=str(input("ingrese la cantidad de agua: "))
agua_1=float(agua)
harina=str(input("ingrese la cantidad de harina: "))
harina_1=float(harina)
sal=str(input("ingrese la cantidad de sal: "))
sal_1=float(sal)/16/3

bol = agua_1 + harina_1 + sal_1
aceite = 1
budare = bol + aceite / 3
print(budare)

input("Dale cualquier tecla para salir")