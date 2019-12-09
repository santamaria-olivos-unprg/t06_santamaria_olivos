# Programa 23

import os

#Declaracion
alumno,cant_faltas="",0

#INPUT

alumno=str(os.sys.argv[1])
cant_faltas=int(os.sys.argv[2])

#PROCESSING
#Condicion multiple

if (cant_faltas >= 7 ):
    print(alumno, "No tienes puntos extras")
if (cant_faltas >= 4 and cant_faltas <= 6):
    print(alumno, "Tienes 1 punto extra")
if (cant_faltas >= 0 and cant_faltas <= 3):
    print(alumno, "Tienes 2 puntos extras")

#fin_if
