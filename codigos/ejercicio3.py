'''3. Analice y realice la prueba de escritorio utilizando el debugger de VSC'''

def mi_funcion(x, y=50): #x vale 10 por la variable a
    '''Parámetros con valores iniciales'''
    print('x:', x) #'x:', 10
    print('y:', y) #'y:', 50

a = int(input('a:')) #10
mi_funcion(a) #pasamos el valor a que vale 10 como argumento de la función
print(mi_funcion.__doc__) #el atributo __doc__ sirve para acceder a los comentarios de la función'''Parámetros con valores iniciales'''

#---------------------------------------------

def f1(): #1 define la función f1
    '''Juan Galan: poeta jujeño 1913-1963'''
    s = '''Jujuy le han puesto de nombre,          
debe ser cosa de Dios; en el idioma del cielo 
así se llama el amor...'''  #3 asigna s una cadena de texto

    def f2():               #4 define la función f2()
        print(s)            #6 imprime s que contiene una cadena de texto
        
    f2()                    #5 llama a la función f2()
f1() #2 llama a la función f1()
print(f1.__doc__)           #6 imprime el comentario del codigo dentro de la función f1()