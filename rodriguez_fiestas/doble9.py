# Programa 09

import os

#Declaracion
nombre,cantidad="",0

#INPUT

nombre=str(os.sys.argv[1])
cantidad=int(os.sys.argv[2])

#PROCESSING
#Por la compra de 3 entradas al cine
#mostrar "¡Ganaste un combo gratis!"
premio=( cantidad > 3 )

if (cantidad > 3):
    print(nombre, "¡Ganaste un combo gratis!")
else:
    print(nombre, "Gracias por su compra")

#fin_if
