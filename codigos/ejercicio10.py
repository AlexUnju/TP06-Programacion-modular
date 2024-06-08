'''10. Diseñar un algoritmo que simule una calculadora básica debe utilizar un módulo denominado calcular(op,a,b)
dónde los parámetros a y b son variables de tipo float y representan los operandos de la expresión aritmética y
op es un parámetro de tipo cadena de caracteres que puede ser: ‘suma’, ‘resta’, ‘multiplicación’ y ‘división’,
y se realiza la operación correspondiente. Mediante un menú de opciones el operador debe ingresar los datos
de a y b y luego debe poder seleccionar una operación aritmética.'''

def calcular(op, a, b):
    """
    Realiza una operación aritmética según el parámetro 'op'.
    'op' puede ser: 'suma', 'resta', 'multiplicación', 'división'.
    'a' y 'b' son los operandos.
    """
    if op == 'suma':
        return a + b
    elif op == 'resta':
        return a - b
    elif op == 'multiplicación':
        return a * b
    elif op == 'división':
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

def menu():
    """Muestra el menú de opciones y maneja la lógica del programa."""
    while True:
        print("\nMenú de la calculadora:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion in {'1', '2', '3', '4'}:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
                continue

            if opcion == '1':
                resultado = calcular('suma', a, b)
                print(f"Resultado de la suma: {resultado}")
            elif opcion == '2':
                resultado = calcular('resta', a, b)
                print(f"Resultado de la resta: {resultado}")
            elif opcion == '3':
                resultado = calcular('multiplicación', a, b)
                print(f"Resultado de la multiplicación: {resultado}")
            elif opcion == '4':
                resultado = calcular('división', a, b)
                print(f"Resultado de la división: {resultado}")
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

# Ejecutar el menú
menu()
