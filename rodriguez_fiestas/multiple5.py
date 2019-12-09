# Programa 25
#Programa para saber en que etapa de la vida se encuentra segun la edad
import os

#Declaracion
edad=0

#INPUT

edad=int(os.sys.argv[1])

#Condicion multiple
if (edad >= 50 ):
    print("Etapa de la Ancianidad!")
if (edad >= 27 and edad <= 49):
    print("Etapa de la Adultez!")
if (edad >= 18 and edad <= 26):
    print("Etapa de la Juventud!")
if (edad >= 12 and edad <= 18):
    print("Etapa de la Adolescencia!")
if (edad >= 6 and edad <= 11):
    print("Etapa de la Infancia!")
if (edad >= 0 and edad <= 5):
    print("Primera infancia!")

#fin_if
