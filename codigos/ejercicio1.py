# 1. ¿Puede explicar con sus propias palabras por qué ambos programas imprimen lo mismo?

#Argumentos Posicionales 
#-----------------------------------------
'''def nombre_persona(nombre, apellido):
    print(f'{nombre} {apellido}')

nombre_persona('Lionel', 'Messi')'''
#------------------------------------------
#Argumentos de palabras claves
'''def nombre_persona(nombre, apellido):
    print(f'{nombre} {apellido}')

nombre_persona(apellido='Messi', nombre='Lionel')'''
#--------------------------------------------

'''
el resultado es el mismo porque la función recibe los mismos valores 
para los mismos parámetros, solo que a través de dos métodos diferentes 
para pasar los argumentos.

En los argumentos posicionales se asignas los valores por las posicion en la que se encuentre los argumentos de 
def nombre_persona(posicion1, posicion2)

En los argumentos por de palabras de claves asignan los valores explicitamente 
nombre_persona(apellido='Messi', nombre='Lionel')}

y con respecto al print lo unico que hace es concatenar las dos variables.

'''