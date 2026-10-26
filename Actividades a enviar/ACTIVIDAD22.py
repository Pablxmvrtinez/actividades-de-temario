print("bienvenido al conversor de monedas tus euros los pasaremos a dolares y a yenes")
euros = float(input())
#primero pedimos en float los euros luego pasaremos los euros a dolares calculando que 1 euro es = a 1,1222 dolares multiplicamos la cantidad
print("perfecto ahora procederemos a la conversion")

dolares = euros * 1.1222
print(dolares)
#aplicamos lo mismo con los yenes
print("ahora pasaremos los euros a yenes")

yenes = euros * 176.11
print(yenes)
print("conclusion tus euros en dolares son", dolares, "y tus euros en yenes son", yenes,)
input()