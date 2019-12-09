# Programa 03

import os

#Declaracion
alumno,nota=" ",0

#INPUT
alumno=str(os.sys.argv[1])
nota=int(os.sys.argv[2])

#PROCESSING
#Si la nota del alumno es mayor a 14
#mostrar "¡Estas aprobado!"
aprobado=(nota >= 14)

if (nota >= 14):
    print(alumno , "¡Estas aprobado!")

