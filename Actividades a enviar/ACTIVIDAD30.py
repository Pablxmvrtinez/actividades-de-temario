

saldo = 1000

while True:
    print("Bienvenido al Banco Santander donde el producto es usted que operacion desea realizar?")
    print("tu saldo es: ", saldo)

    print("que opcion deseas realizar elige la opcion escribiendo solo el numero")
    print("1.Ingresar saldo")
    print("2.Retirar saldo")
    print("3.Consultar saldo")
    print("4.Salir")
    accion = int(input())

    if accion == 1:
        print("okey cuanto saldo deseas ingresar?")
        ingreso = int(input())
        saldo = ingreso + saldo
        print("perfecto se ingresara",ingreso)
        print("su nuevo saldo es",saldo)

    elif accion == 2:
       
        print("Okey cuanto saldo deseas retirar?")
        retirar = int(input())
        if saldo < retirar:
            print("Saldo insuficiente intentelo de nuevo")
        else:

            saldo = saldo - retirar
            print("perfecto se le retirara",retirar)
            print("su nuevo saldo es",saldo)
   
    elif accion == 3:
        if saldo == 1000:
            print("su saldo sigue siendo: ", saldo)
        if saldo != 1000:
            print("tu saldo actual ha cambiado a", saldo)

    elif accion == 4:
        print("perfecto finalizanco operaciones")
        break
