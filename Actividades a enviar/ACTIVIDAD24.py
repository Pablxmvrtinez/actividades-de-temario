print("Verificador de partes fraccionarias")
print("Introduce un número para comprobarlo:")

numero = float(input())

entero = int(numero)

if numero != entero:
    print("Tu número tiene parte fraccionaria")
else:
    print("Tu número NO tiene parte fraccionaria")
    input()
    