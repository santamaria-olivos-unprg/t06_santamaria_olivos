#Programa19:Ingrese una edad de una persona
import os

#Declaración
apellidos=" "
edad=0

#Input vis os
apellidos=os.sys.argv[1]
edad=int(os.sys.argv[2])

#Processing
#Diga si tienes dni amarillo o azul
#Mostrar:Tiene DNI azul
#Mostrar:Tiene DNI amarillo
if (edad >= 18):
    print(apellidos,"Tiene DNI azul")
else:
    print(apellidos,"Tiene DNI amarillo")

#fin_if
