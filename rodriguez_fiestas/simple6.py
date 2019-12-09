# Programa 06

#Dado la cantidad polos de la tienda "ClaireKids"
import os

#Declaracion
nombre,cantidad="",0

#INPUT

nombre=str(os.sys.argv[1])
cantidad=int(os.sys.argv[2])

#PROCESSING
#Si la compra es superior a 3 polos
#mostrar "¡Te llevas un short gratis!"
premio=( cantidad > 3)

if (cantidad > 3):
    print(nombre, "¡Te llevas un short gratis!")
