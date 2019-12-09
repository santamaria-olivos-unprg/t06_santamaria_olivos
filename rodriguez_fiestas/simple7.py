# Programa 07

import os

#Declaracion
nombre,cantidad="",0

#INPUT

nombre=str(os.sys.argv[1])
cantidad=int(os.sys.argv[2])

#PROCESSING
#Si la compra es mayor de 3 panetones
#mostrar "¡Ganaste una tableta de chocolate!"
premio=( cantidad > 3 )

if (cantidad > 3):
    print(nombre, "¡Ganaste una tableta de chocolate!")
