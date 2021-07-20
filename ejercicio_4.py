# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese tres palabras y arme un acrónimo con ellas
# Si desea puede modificar el código para ingresar más palabras
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

print('Ingrese palabra 3:')
palabra_3 = str(input())

print(palabra_1 + " " + palabra_2 + " " + palabra_3)

#anacron = "computer science engineering"
anacron = str(palabra_1 + " " + palabra_2 + " " + palabra_3)

def fxn(stgn):

    oupt= stgn[0]

    for i in range(1,len(stgn)):
        if stgn[i-1] == " ":

            oupt += stgn[i]
    oupt = oupt.upper()
    return oupt        


print(fxn(anacron))


# De cada palabra debe tomar la primera letra y armar el acrónimo
# Ejemplo: Alumbrado, barrido y limpieza --> ABL
# Imprimir el resultado en pantalla
