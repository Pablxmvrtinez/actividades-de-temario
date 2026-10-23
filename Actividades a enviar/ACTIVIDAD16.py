#Primero se printea y se pone el input
print("introduzca el año para comprobar si es bisiesto")
año = int(input())
print("perfecto ahora calcularemos si es bisiesto")

#usamos if % == para comprobar sus restos y != para que 
#entienda que no puede ser divisible entre 100 
#tambien elif para que pille si es divisible entre 400
if año % 4 == 0 and año % 100 != 0:

    print("es bisiesto")

elif año % 400 == 0:
    print("es bisiesto")

else:
    print("no es bisiesto")
