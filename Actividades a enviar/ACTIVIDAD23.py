print("programa para saber si un numero tiene 3 cifras o no a continuacion escribe su numero a evaluar")
#pides la cifra usas if y >= o <= poco mas 
cifra = int(input())

if cifra <= 999 and cifra >= 100:
    print("tu numero tiene 3 cifras")
elif cifra >= -999 and cifra <= -100:
    print("tiene 3 cifras pensabas que me ibas a pillar con los negativos eh")
else:
    print("tu numero no tiene 3 cifras")