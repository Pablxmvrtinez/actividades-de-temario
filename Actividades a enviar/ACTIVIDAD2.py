# primero le pedimso que introduzca los dos numeros OJO aqui ponemos con el input un int para crear numeros enteros sin decimales
print("Buenas porfavor muestreme su primer numero")
numero1 = int(input())
print("ahora el numero 2")
numero2 = int(input())
# cuando el usuario los añada surge la magia por que printearemos para recordarle sus numeros y luego usaremos los valores creados con anterioridad
# para printear los resultados
print("perfecto sus numeros son: ")

print(numero1)
print(numero2)

print("perfecto ahora procedemos con las operaciones")
print("la suma es: ")
suma = numero1 + numero2
print(suma)

print("la resta es: ")
resta = numero1 - numero2 
print(resta)

print("la multiplicasao es: ")
multiplicacion = numero1 * numero2
print(multiplicacion)

print("la division es: ")
division = numero1 / numero2
print(division)
#este input esta para q no se cierre el cmd automaticamente y puedas ver los resultados
input()