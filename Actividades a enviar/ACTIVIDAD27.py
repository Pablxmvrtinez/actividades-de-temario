print("primero dame la fecha siguiendo el siguiente orden: dia mes año")
dia = int(input())
mes = int(input())
año = int(input())
print("perfecto ahora me encargare de dartelo mas extenso ")
#para esto basicamente pedimos las fechas y luego entre comillas ponemos las frases con los valores y le ponemos comas para que no salte error usamos == para que iguale
if mes == 1:
    print("Su fecha es ", dia, "de enero de", año)
elif mes == 2:
    print("Su fecha es ", dia, "de febrero de", año)
elif mes == 3:
    print("Su fecha es ", dia, "de marzo de", año)
elif mes == 4:
    print("Su fecha es ", dia, "de abril de", año)
elif mes == 5:
    print("Su fecha es ", dia, "de mayo de", año)
elif mes == 6:
    print("Su fecha es ", dia, "de junio de", año)
elif mes == 7:
        print("Su fecha es ", dia, "de julio de", año)
elif mes == 8:
    print("Su fecha es ", dia, "de agosto de", año)
elif mes == 9:
    print("Su fecha es ", dia, "de septiembre de", año)
elif mes == 10:
    print("Su fecha es ", dia, "de octubre de", año)
elif mes == 11:
    print("Su fecha es ", dia, "de noviembre de", año)
elif mes == 12:
    print("Su fecha es ", dia, "de diciembre de", año)
else:
    print("algun valor ha sido escrito de manera erronea porfavor intentalo de nuevo los numeros se ponen sin 0 los que abarcan desde enero hasta septiembre")
    input()


    