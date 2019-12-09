# Programa 18

import os

#Declaracion
alumno,cant_faltas="",0

#INPUT

alumno=str(os.sys.argv[1])
cant_faltas=int(os.sys.argv[2])

#PROCESSING
#Si el alumno supera las 4 faltas
#mostrar "Estas desaprobado"
desaprobado=( cant_faltas > 4 )

if (cant_faltas > 4):
    print(alumno, "Estas desaprobado")
else:
    print(alumno, "Tienes 2 puntos extras")

#fin_if
