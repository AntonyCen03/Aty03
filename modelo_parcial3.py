#Tu teclado de la laptop está defectuoso, y cada vez que escribes el carácter
#'i', se invierte la cadena que has escrito. Escribir otros caracteres funciona como se
#espera. Se te da una cadena s indexada a partir de 0, y escribes cada carácter de s
#usando tu teclado defectuoso. Devuelve la cadena final que aparecerá en la pantalla
#de tu laptop.

def laptop_defectuoso(palabra):
    output=""
    for j in palabra:
        if j=="i":
            output=output[::-1]
        else:
            output+=j
    return output

s = "string" #input
#output="rtsng"

resultado=laptop_defectuoso(s)
print(resultado)
