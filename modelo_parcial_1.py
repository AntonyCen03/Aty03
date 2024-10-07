#Dadas dos listas de strings word1 y word2, devuelve True si las dos listas
#representan la misma cadena, y False en caso contrario. Una cadena está
#representada por una lista si los elementos de la lista concatenados en orden
#forman la cadena

word1 = ["ab", "c"]
word2 = ["a", "bc"]

def cadena_igual(cadena1,cadena2):
    if "".join(cadena1)=="".join(cadena2):
        return True
    else:
        return False
    
cadena_resultado=cadena_igual(word1,word2)
print(cadena_resultado)
