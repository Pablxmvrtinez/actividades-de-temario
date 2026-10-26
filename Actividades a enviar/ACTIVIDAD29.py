print("vamos a calcular la edad exacta en años meses y dias primero mandame tu fecha de nacimiento empieza por dia sigue en meses acaba en años")

dia = int(input())
mes = int(input())
año = int(input())

print("perfecto ahora vamos a calcularlo pero antes pasame la fecha  en la que realizas la conversion en el mismo orden que antes")

dia2 = int(input())
mes2 = int(input())
año2 = int(input())

print("perfecto ahora haremos unos calculos")

añoF = año2 - año
mesF = mes2 - mes
diaF = dia2 - dia

if diaF < 0:
    diaF += 30
    mesF -= 1

if mesF < 0:
    mesF += 12
    añoF -= 1

print("Tienes", añoF, "años,", mesF, "meses y", diaF, "días")

