#primero le pedimos el peso y estatura usamos float ya que normalmente
#tanto el peso como estatura suelen ser numeros decimales
print("bienvenido a la calculadora de imc ponga a continuacion el peso y su estatura")
peso = float(input())
estatura = float(input())

estatura2 = estatura ** 2

imc = peso / estatura2
#despues hacemos la formula del imc usamos ** cuando reflejamos que se eleva no multiplica

print("perfecto su imc es :")
print(imc)

#por ultimo usamos if para poner cada condicion de el imc dependiendo del resultado
if imc <= 18.5:
    print(imc, "estas bajo de peso")
elif imc >= 18.5 and imc <= 24.9:
    print(imc, "peso saludable")
elif imc >= 25.0 and imc <= 29.9:
    print(imc, "tienes sobre peso")
elif imc >= 30.0 and imc <= 34.9:
    print(imc, "tienes sobre peso grado 1")
elif imc >= 35.0 and imc <= 39.9:
    print(imc, "tienes sobre peso grado 2")
elif imc >= 40:
    print(imc, "obesidad grado 3/obesidad morbida")
    
    input()