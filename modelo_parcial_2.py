#Hay n empleados en una empresa, numerados del 0 al n - 1. El i-ésimo
#empleado ha trabajado hours[i] horas en la empresa. La empresa requiere que cada
#empleado trabaje al menos target horas. Se te da una lista de enteros no negativos
#hours de longitud n y un entero no negativo target. Devuelve el número de
#empleados que trabajaron al menos target horas.

hours = [0,1,2,3,4]
target=2
def empresa(horas,tiempo):
    j=0
    objetivo_cumplito=[]
    for i in horas:
        if i+j>=tiempo:
            objetivo_cumplito.append(i+j)
    return objetivo_cumplito

empleado_aprovado=empresa(hours,target)
print(f"los empleado que trabaje mayor o igual a 2 horas son: {len(empleado_aprovado)}")
