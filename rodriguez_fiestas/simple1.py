# Programa 01

import os

#Declaracion
nombre,edad=" ",0

#INPUT
nombre=str(os.sys.argv[1])
edad=int(os.sys.argv[2])

#PROCESSING
#Si el usuario es menor de edad no podra entrar al cine
#mostrar "¡Hasta la proxima!"
menor_edad=(edad < 18)

if (edad < 18):
    print(nombre , "¡Hasta la proxima!")

