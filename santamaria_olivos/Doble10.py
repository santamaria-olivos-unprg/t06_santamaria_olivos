#Programa20:Dado el promedio obtenido en 5to de secundaria
import os

#Declaraciones
alumno=" "
prom=0.0

#Input vis os
alumno=os.sys.argv[1]
prom_final=float(os.sys.argv[2])

#Processing
#Si su promedio el mayor o igual a 18
#Mostrar:SE GANO UNA BECA!!
#Mostrar:No alcanzo la beca
if(prom_final>=17):
    print(alumno,"SE GANO UNA BECA")
else:
    print(alumno,"No alcanzo la beca")

#fin_if
