#Programa29:Ingrese una edad de una persona
import os

#Declaración
apellidos=" "
edad=0

#Input vis os
apellidos=os.sys.argv[1]
edad=int(os.sys.argv[2])

#Processing
#Si tiene 1año a 6años (esta en la etapa de la infancia)
if (edad>=1 and edad<=5):
    print(apellidos,"Esta en la etapa de la Infancia ")
#Si tiene 6año a 12años (Esta en la etapa de la niñez)
if (edad>=6 and edad1<=12):
    print(apellidos,"Esta en la etapa de la Niñez")
#Si tiene 13año a 20años (Esta en la etapa de la adolescencia)
if (edad>=13 and edad<=20):
    print(apellidos,"Esta en la etapa de la Adolescencia")
#Si tiene 21año a 2años (Esta en la etapa de la juventud)
if (edad>=21 and edad<=25):
    print(apellidos,"Esta en la etapa de la Juventud")
#Si tiene 26 años a 60años (Esta en la etapa de la adultez)
if (edad>=26 and edad<=60):
    print(apellidos,"Esta en la etapa de la Adultez")
#Si tiene mas 60años (Esta en la etapa de la ancianidad)
if (edad>60):
    print(apellidos,"Esta en la etapa de la Ancianidad")
#Si tiene dni amarillo tiene menos 18años
if (edad >= 18):
    print(apellidos,"Tiene DNI azul")
#Si tiene dni azul tiene >= 18años
if (edad<18):
    print(apellidos,"Tiene DNI amarillo")

#fin_if
