# Programa 10

import os

#Declaracion
nombre,calificacion="",0

#INPUT

nombre=str(os.sys.argv[1])
calificacion=int(os.sys.argv[2])

#PROCESSING
#Si la calificacion es mayor a 11
#mostrar "¡Estas exonerado!"
premio=( calificacion > 11 )

if (calificacion > 11):
    print(nombre, "¡Estas exonerado!")
