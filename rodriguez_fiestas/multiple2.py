# Programa 22

import os

#Dado el nro de tickets obtenidos en Coney Park
import os

#Declaracion
nombre,nro_tickets="",0

#INPUT
nombre=str(os.sys.argv[1])
nro_tickets=int(os.sys.argv[2])

#Condicion multiple
#Si el nro tickets >= 2000 (¡Ganaste un peluche!)
if (nro_tickets >= 1501):
    print(nombre,"¡Ganaste un peluche!")
#Si el nro tickets >= 501 y 1500 (¡Ganaste un yoyo!)
if (nro_tickets >= 501 and nro_tickets <= 1500):
    print((nombre,"¡Ganaste un yoyo!"))
#Si el nro tickets >= 0 y 500(¡Sigue intentando!)
if (nro_tickets >= 0 and nro_tickets <= 500):
    print((nombre,"¡Sigue intentando!"))

#fin_if
