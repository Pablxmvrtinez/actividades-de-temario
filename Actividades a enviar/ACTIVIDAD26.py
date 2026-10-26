#pedimos la palabra
print("Programa para comprobar si la palabra es un palindromo")
palabra = input().lower()
#creamos una variable con un comando que ni sabia que existia que le da la vuelta a la palabra
print("perfecto vamos a la comprobación")
invertida = (palabra[::-1])
#usamos el if
if invertida == palabra:
    print("en efecto es palindromo")

else:
    print("no es palindromo")

input()

