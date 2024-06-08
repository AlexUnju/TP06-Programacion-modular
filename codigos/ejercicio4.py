''''4. Analizar y ejecutar el algoritmo que calcula la serie de Taylor de la función seno de más abajo, dónde x es el
valor de un ángulo (expresado en radianes) y n es el número de términos. Mostrar el esquema de los módulos
según la programación modular, y los ámbitos de las variables. También hacer la prueba de escritorio para un
ángulo de 45 grados sexagesimales y 4 términos, utilice el debugger del VSC.
'''
import math  # Importar el módulo math para la función pi y sin

def bienvenida (n): #1 define la función bienvenida #8 el valor de la variable nombre se asigna a la variable n nombre => n
    nro = 20 #9 asigna
    car = '-' #10 asigna
    print(car*nro)  #11 imprime el resultado de la multiplicación, deberia dar un "-" 20 veces
    print('Hola ', n) #12 imprime un mensaje 'hola ' + la el string de n
    print(car*nro) #13 imprime el resultado de la multiplicación, deberia dar un "-" 20 veces
    print('Este algoritmo calcula el seno ') #14 imprime el mensaje
    print('de un ángulo en grado sexagesimal') #15 imprime el mensaje
    print('con la serie de Taylor hasta un ') #16 imprime el mensaje
    print('término determinado por Ud. ') #17 imprime el mensaje
    print(car*nro) #18 imprime el resultado de la multiplicación, deberia dar un "-" 20 veces

def verificaP(): #2 define la función verificarP
    while True: #21 se ejecuta el bucle
        x = float(input('Ángulo en sexagesimales x>=0:')) #22 ingresamos un valor de tipo float a la variable x
        if x >= 0: #23 lee la condición 
            return x #24 si la condición se cumple el bucle termina, de lo contrario volverá a pedir que se ingrese un dato float de la variable x
    
def verificaMenor10(): #3 define la función verificarMenor10 
    while True: #28 se ejecuta el bucle
        m10 = int(input('N° de términos [1,10]:')) #29 m10 se asigna con un valor de entrada de tipo número entero
        if m10 >= 1 and m10 <= 10: #30 lee la condición
            return m10 #31 si la condición se cumple el bucle termina, de lo contrario volverá a pedir que ingrese un numero entero para la variable m10
        
def factorial(x):   #4 define la función factorial #41 el argumento de la función pasa ser t
    p = 1 #42 se asigna p
    for i in range(1, x+1): #44 se ejecuta el bucle for
        p *= i #45 se multiplica p por i
    return p #46 retorna p y se termina el bucle

def potencia(base, exponente): #5 define la función potencia #36 los argumentos de la funcion pasan a ser -1 y n
    p = 1 #37 se asigna un valor a p
    for i in range(exponente): #38 se ejecuta el bucle for
        p *= base   #39 se multiplica p por base
    return p #40 retorna p y se termina el for

#Principal
nombre = input('Ingrese su nombre:') #6 ingresa dato de tipo string a nuestra variable de entrada
bienvenida(nombre) #7 llamamos a nuestra función bienvenida con la variable nombre como argumento #19 salimos de la función
a = verificaP() #20 asignamos a la variable a la funcion verificarP y automaticamente se llama a la función #25 la función se termina
x = a*math.pi/180 #radianes #26 se asigna x con el valor asignado
m = verificaMenor10() #valor final términos #27 asignamos m la función de verificaMenor10()
suma = 0 #32 se asigna a suma 0
for n in range(m): #33 se ejecuta el bucle for
    t = 2*n+1   #34 se asigna un valor a t
    suma += potencia(-1,n)/factorial(t)*potencia(x,t) #35 suma se incrementa por el valor de las funciones y llama a la función potencia y factorial

print('Seno calculado = ', suma)    #47 imprime un mensaje 'Seno calculado = ' + suma
print('Seno función interna = ',math.sin(x)) #48 imprime un mensaje 'Seno función interna = ' + sin(x)