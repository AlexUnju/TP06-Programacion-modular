'''7. Escribir un módulo denominado PMS que tiene dos parámetros formales base y exponente. Calcular la base
elevada al exponente, siendo la base un número real cualquiera y exponente un valor entero positivo o nulo.
Utilizar las multiplicaciones sucesivas de la base. Si el cálculo no puede realizarse debe devolver cero (0).
'''

def PMS(base, exponente):
    """
    Calcula la potencia de una base elevada a un exponente utilizando multiplicaciones sucesivas.
    
    Parámetros:
    base (float): El número base.
    exponente (int): El exponente al que se elevará la base. Debe ser un entero positivo o nulo.
    
    Retorna:
    float: El resultado de base^exponente, o 0 si el cálculo no puede realizarse.
    """
    # Verificar si el exponente es negativo
    if exponente < 0:
        return 0
    
    # Caso especial: cualquier número elevado a la potencia de 0 es 1
    if exponente == 0:
        return 1
    
    # Iniciar el resultado como 1 (la identidad multiplicativa)
    resultado = 1
    
    # Realizar las multiplicaciones sucesivas
    for _ in range(exponente):
        resultado *= base
    
    return resultado

# Ejemplos de uso
print(PMS(2, 3))  # Debería imprimir 8
print(PMS(5, 0))  # Debería imprimir 1
print(PMS(7, -2)) # Debería imprimir 0
print(PMS(3, 4))  # Debería imprimir 81
