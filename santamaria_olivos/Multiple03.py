#Programa23: Dado el promedio obtenido en 5to de secundaria
import os

#Declaraciones
alumno=" "
prom=0.0

#Input vis os
alumno=os.sys.argv[1]
prom_final=float(os.sys.argv[2])

#Processing
#Si su promedio es mayor o igual a 17 (Ganó una beca)
if(prom_final>=17):
    print(alumno,"SE GANO UNA BECA")
#Si su promedio es menor a 17 (No alcanzo la beca)
if(prom_final<=15):
    print(alumno,"No alcanzo la beca")
#Si su promedio es menor < 14
if(prom_final<14):
    print(alumno,"Siga intentando")
#Si su promedio es menor < 11
if(prom_final<11):
    print(alumno,"Su promedio es muy bajo")

#fin_if

