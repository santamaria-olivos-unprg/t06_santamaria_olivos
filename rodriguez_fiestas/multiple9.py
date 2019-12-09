#Programa 29
#Ingresar el sueldo de una persona,si el sueldo es menor a 1500 soles, mostrar un mensaje
import os

#Declaracion
nombre,sueldo="", 0.0

#INPUT

nombre=str(os.sys.argv[1])
sueldo=int(os.sys.argv[2])

#Condicion multiple
if (sueldo < 1500):
    print(nombre, "¡No pagara impuestos!")
if (sueldo > 1500 and sueldo < 2500):
    print(nombre, "¡Pagara 10% de su sueldo!")
if (sueldo >= 2500 ):
    print(nombre,"¡Pagara impuestos!")

#fin_if
