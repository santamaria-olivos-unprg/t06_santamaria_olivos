#Programa15: Si compra un celular Huawei en Ripley
import os
#Detectores
cliente=" "
celular=" "

#INPUT vis OS
cliente=os.sys.argv[1]
celular=os.sys.argv[2]

#PROCESSING
#Si el celular es HUAWEI tiene descuento más una mochila gratis
#Mostrar, Tienes descuento más una mochila gratis!!
#Mostrar, gracias por su compra
if (celular=="Huawei"):
    print(cliente,"Tiene descuento más una mochila gratis")
else:
    print(cliente,"Gracias por su compra")

#fin_if
