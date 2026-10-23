print("vamos a verificar si un numero es par o impar introduzca su numero")
numero = int(input())
print("perfecto ahora con una simple operacion lo descubriremos")

# declaramos a numero como int con input para que puedan darle el valor que quieras y usamos if y else para que dependiendo del resultado nos de si  es par o no
if numero % 2 == 0:
    print("el numero es par")
else:
    print("es inpar")
    input()



