#Programa 30
#Ingresar el nombre del empleado y el nro de productos vendidos
import os

#Declaracion
nombre,nro_productos="", 0

#INPUT

nombre=str(os.sys.argv[1])
nro_productos=int(os.sys.argv[2])

#Condicion multiple
if (nro_productos >= 13):
    print(nombre,"Empleado Excelente!")
if (nro_productos >= 8 and nro_productos<= 12):
    print(nombre,"Empleado Bueno!")
if (nro_productos >= 1 and nro_productos <= 7):
    print(nombre,"Empleado Regular!")

#fin_if
