# Programa 24

import os

#Declaracion
nombre,calificacion="",0

#INPUT

nombre=str(os.sys.argv[1])
calificacion=int(os.sys.argv[2])

#Condicion multiple
if (calificacion >= 16):
    print(nombre, "¡Estas exonerado!")
if (calificacion >= 9 and calificacion <= 15):
    print(nombre, "¡Con fe al susti!")
if (calificacion >= 0 and calificacion <= 8):
    print(nombre, "¡Estas desaprobado!")

#fin_if
