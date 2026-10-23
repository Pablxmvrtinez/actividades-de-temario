print("bienvenido al conversor de segundos --> minutos --> horas porfavor introduzca los segundos")
segundos = int(input())
print("perfecto los segundos en minutos serian")

minutos = segundos // 60
minutosysegundos = segundos % 60
print(minutos, "minutos y" ,minutosysegundos, "segundos")

input()