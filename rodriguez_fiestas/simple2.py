# Programa 02

#Dado el nro de tickets obtenidos en Coney Park
import os

#Declaracion
nombre,nro_tickets="",0

#INPUT
nombre=str(os.sys.argv[1])
nro_tickets=int(os.sys.argv[2])

#PROCESSING
#Si el nro de tickets supera los 150
#mostrar "¡Ganaste un yoyo!"
if (nro_tickets > 150):
    print(nombre, "¡Ganaste un yoyo!")
