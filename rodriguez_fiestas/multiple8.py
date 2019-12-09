#Programa 28
#Declarar la edad para saber cuando deben pagar para entrar al cine
import os

#Declaracion
edad=0

#INPUT

edad=int(os.sys.argv[1])

#Condicion multiple
if (edad >= 61):
    print("¡Pagan 14 soles!")
if (edad >= 3 and edad <= 60):
    print("¡Pagan 17 soles!")
if (edad >= 0  and edad <= 2):
    print("¡No pagan!")

#fin_if
