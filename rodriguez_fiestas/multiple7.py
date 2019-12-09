#Programa 27

import os

#Declaracion
velocidad_auto=0

#INPUT

velocidad_auto=int(os.sys.argv[1])

#Condicion multiple
if (velocidad_auto >= 91):
    print("¡Exceso de velocidad!")
if (velocidad_auto >= 61 and velocidad_auto <= 90):
    print("¡Velocidad Regular!")
if (velocidad_auto >= 0  and velocidad_auto<= 60):
    print("¡Velocidad Minima!")

#fin_if
