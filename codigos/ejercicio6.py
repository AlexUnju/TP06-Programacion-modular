'''Escribir un módulo que utiliza tres parámetros que representan un ancho y altura, el tercer
parámetro es un carácter a utilizar en el dibujo de un rectángulo. En el ejemplo siguiente se
leen los valores 5 (ancho), 3 (altura) con el carácter “o”, resultando el gráfico:
'''

def dibujar_rectangulo(ancho, altura, caracter):
    # Iterar sobre la altura del rectángulo
    for i in range(altura):
        # Imprimir una fila del rectángulo
        print(caracter * ancho)

# Programa principal
# Leer los valores de ancho, altura y carácter
ancho = int(input('Ingrese el ancho del rectángulo: '))
altura = int(input('Ingrese la altura del rectángulo: '))
caracter = input('Ingrese el carácter para dibujar el rectángulo: ')

# Llamar a la función para dibujar el rectángulo
dibujar_rectangulo(ancho, altura, caracter)
