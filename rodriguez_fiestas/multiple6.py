# Programa 26
#Programa para saber en que division de futbol perteneces
import os

#Declaracion
edad=0

#INPUT

edad=int(os.sys.argv[1])

#Condicion multiple
if (edad >= 22):
    print("¡Primera division!")
if (edad >= 18 and edad <= 21):
    print("¡Segunda division!")
if (edad >= 13  and edad <= 17):
    print("¡Tercera division!")

#fin_if
