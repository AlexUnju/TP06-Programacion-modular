'''11. Escribir un algoritmo que simule las operaciones que se realizan en un cajero automático de acuerdo al
esquema jerárquico de los módulos que se nota en la figura:
'''
def cajeroAutomatico():
    while True:
        print("Ingresa las opciones:")
        print(guiones*20);
        opcionIngresada = int(input(" [1] INGRESAR CLAVE \n [2] SALIR \n OPCION ELEJIDA: "))
        print(guiones*20);
        if opcionIngresada == 1:
            lecturaValidacionClave();
            break
        elif opcionIngresada == 2:
            finalizar();
            break
        else:
             print("Opción no valida")
             
def lecturaValidacionClave() :
        clave = 1234;
        intentos = 3;
        while intentos > 0:
                print("Intentos permitidos:", intentos);
                claveIngresada = int(input("Ingrese la clave: "));
                if claveIngresada == clave:
                    print("Contraseña correcta");
                    operacion()
                else:
                    intentos -= 1;
                    print("Contraseña incorrecta.");
        
        print("Intentos superados, vuelva mas tarde.")
        return False;
                


def operacion():
        while True:
            print(guiones*20);
            print("¿Que operación desea realizar?");
            print(" [1] Consulta de saldo \n [2] Retiro de efectivo \n [3] Deposito \n [4] SALIR");
            opcionIngresada=int(input("OPCION ELEJIDA: "))

            if opcionIngresada == 1:
                  consultaSaldo();
                  break;
            elif opcionIngresada == 2:
                 retiroEfectivo();
                 break;
            elif opcionIngresada == 3:
                 deposito();
                 break;
            elif opcionIngresada == 4:
                 finalizar();
                 break;
            else:
                 print(guiones*20);
                 print("Opción no valida, intente de nuevo.")
                

def finalizar() :
        print("Gracias por usar nuestro Cajero automatico :D")
        return
            
def consultaSaldo() :
    global saldo;
    print("Su saldo es de: ", saldo)
    operacion()
    return

def retiroEfectivo() :
    global saldo;
    while True:
        retiroEfectivo = int(input("Ingrese la cantidad de efectivo que desea retirar: "))
        if retiroEfectivo > 0 and retiroEfectivo < saldo:
             saldo -= retiroEfectivo;
             break
        elif retiroEfectivo > saldo:
            print("Fondos insuficientes. Intente con una cantidad menor.")
        else:
             print("El retiro debe ser mayor que 0")
    print("¡operacion realizada!")
    return operacion();


def deposito():
    global saldo;
    while True:
        depositoEfectivo = int(input("Ingrese la cantidad de dinero que desea depositar: "))
        if depositoEfectivo > 0:
             saldo += depositoEfectivo;
             operacion();
             break;
        else:
             print("El deposito debe ser mayor que 0")
    print("¡operacion realizada!")
    return
             


#PRINCIPAL
guiones= "-";
saldo = 1000;
cajeroAutomatico()
