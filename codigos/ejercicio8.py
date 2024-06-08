'''8. Mediante un menú de opciones resolver:
a. Ingresar dos valores a y b validando que estén en el intervalo [0,9] y mostrarlos en letras separados por
una serie de asteriscos
b. Si a y b son pares intercambiar los valores y mostrarlos en letras'''

def numero_a_letras(n):
    """
    Convierte un número en el rango [0, 9] a su representación en letras.
    """
    numeros_en_letras = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    return numeros_en_letras[n]

def validar_valor(n):
    """
    Valida que un número esté en el rango [0, 9].
    """
    return 0 <= n <= 9

def mostrar_numeros_en_letras(a, b):
    """
    Muestra los números a y b en letras separados por una serie de asteriscos.
    """
    a_letras = numero_a_letras(a)
    b_letras = numero_a_letras(b)
    print(f"{a_letras} *** {b_letras}")

def intercambiar_si_pares(a, b):
    """
    Intercambia los valores de a y b si ambos son pares y los muestra en letras.
    """
    if a % 2 == 0 and b % 2 == 0:
        a, b = b, a
    mostrar_numeros_en_letras(a, b)

def menu():
    """
    Muestra el menú de opciones y maneja la lógica del programa.
    """
    while True:
        print("\nMenú de opciones:")
        print("1. Ingresar dos valores y mostrarlos en letras")
        print("2. Intercambiar valores si ambos son pares y mostrarlos en letras")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            a = int(input("Ingrese el valor de a (0-9): "))
            b = int(input("Ingrese el valor de b (0-9): "))
            if validar_valor(a) and validar_valor(b):
                mostrar_numeros_en_letras(a, b)
            else:
                print("Valores fuera del rango permitido.")
        elif opcion == '2':
            a = int(input("Ingrese el valor de a (0-9): "))
            b = int(input("Ingrese el valor de b (0-9): "))
            if validar_valor(a) and validar_valor(b):
                intercambiar_si_pares(a, b)
            else:
                print("Valores fuera del rango permitido.")
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")

# Ejecutar el menú
menu()
