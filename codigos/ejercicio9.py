'''9. Realizar un programa modular que muestre un menú de opciones. Debe ingresar inicialmente dos valores que
representan el numerador y denominador de una fracción.

a. sumar_fracciones(n1,d1,n2,d2) calcula la suma de dos fracciones. El resultado es otra fracción cuyo
numerador es n1*d2+d1*n2 y denominador d1*d2. Se debe simplificar la fracción resultado.

b. restar_fracciones(n1,d1,n2,d2) calcula la resta de dos fracciones. El resultado es otra fracción
numerador=n1*d2-d1*n2 y denominador=d1*d2. Se debe simplificar la fracción resultado.

c. multiplicar_fracciones(n1,d1,n2,d2) calcula el producto de dos fracciones. El resultado es una fracción
con numerador n1*n2 y denominador d1*d2. Se debe simplificar la fracción resultado.

d. dividir_fracciones(n1,d1,n2,d2) calcula la división de dos fracciones. El resultado es una fracción con
numerador n1*d2 y denominador d1*n2. Se debe simplificar la fracción resultado.

En cada ejecución del programa deberá ingresar la fracción solicitando numerador y denominador. La fracción
debe simplificarse y mostrarse.
Al mostrar la fracción se debe mostrar la misma simplificada. En caso de denominador 1, sólo debe mostrar el
numerador.
Puede implementar una función simplificar_funcion(n,d) que devuelve 2 nuevos valores resultados de la
simplificación, para ello hay que dividir n y d por el mcd de ambos.
Puede implementar una función mcd(n,d) que devuelve el máximo común divisor de ambos parámetros.
'''

def mcd(a, b):
    """Calcula el máximo común divisor de a y b."""
    while b:
        a, b = b, a % b
    return a

def simplificar_fraccion(n, d):
    """Simplifica la fracción (n/d) dividiendo ambos por su MCD."""
    divisor_comun = mcd(n, d)
    return n // divisor_comun, d // divisor_comun

def sumar_fracciones(n1, d1, n2, d2):
    """Suma dos fracciones y devuelve el resultado simplificado."""
    num = n1 * d2 + d1 * n2
    den = d1 * d2
    return simplificar_fraccion(num, den)

def restar_fracciones(n1, d1, n2, d2):
    """Resta dos fracciones y devuelve el resultado simplificado."""
    num = n1 * d2 - d1 * n2
    den = d1 * d2
    return simplificar_fraccion(num, den)

def multiplicar_fracciones(n1, d1, n2, d2):
    """Multiplica dos fracciones y devuelve el resultado simplificado."""
    num = n1 * n2
    den = d1 * d2
    return simplificar_fraccion(num, den)

def dividir_fracciones(n1, d1, n2, d2):
    """Divide dos fracciones y devuelve el resultado simplificado."""
    num = n1 * d2
    den = d1 * n2
    return simplificar_fraccion(num, den)

def mostrar_fraccion(n, d):
    """Muestra la fracción simplificada, omitiendo el denominador si es 1."""
    if d == 1:
        print(n)
    else:
        print(f"{n}/{d}")

def menu():
    """Muestra el menú de opciones y maneja la lógica del programa."""
    while True:
        print("\nMenú de opciones:")
        print("1. Sumar fracciones")
        print("2. Restar fracciones")
        print("3. Multiplicar fracciones")
        print("4. Dividir fracciones")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in {'1', '2', '3', '4'}:
            n1 = int(input("Ingrese el numerador de la primera fracción: "))
            d1 = int(input("Ingrese el denominador de la primera fracción: "))
            n2 = int(input("Ingrese el numerador de la segunda fracción: "))
            d2 = int(input("Ingrese el denominador de la segunda fracción: "))

            if d1 == 0 or d2 == 0:
                print("El denominador no puede ser 0.")
                continue

            if opcion == '1':
                num, den = sumar_fracciones(n1, d1, n2, d2)
                print("Resultado de la suma: ", end="")
                mostrar_fraccion(num, den)
            elif opcion == '2':
                num, den = restar_fracciones(n1, d1, n2, d2)
                print("Resultado de la resta: ", end="")
                mostrar_fraccion(num, den)
            elif opcion == '3':
                num, den = multiplicar_fracciones(n1, d1, n2, d2)
                print("Resultado de la multiplicación: ", end="")
                mostrar_fraccion(num, den)
            elif opcion == '4':
                num, den = dividir_fracciones(n1, d1, n2, d2)
                print("Resultado de la división: ", end="")
                mostrar_fraccion(num, den)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

# Ejecutar el menú
menu()
