#Programa8:Solicite el precio de las marca de 2 polos
import os

#Declaración
polo1=" "
polo2=" "
precio1=0.0
precio2=0.0

#Input vis os
polo1=os.sys.argv[1]
precio1=float(os.sys.argv[2])
polo2=os.sys.argv[3]
precio2=float(os.sys.argv[4])

#Processing
#Si el precio 1 es mayor que el precio2
#Mostrar: El precio del polo1 es mayor que el de polo2
if(precio1 > precio2):
    print("El precio del polo",polo1,"es mayor que del de",polo2)

#fin_if
