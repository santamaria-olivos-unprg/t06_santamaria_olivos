#Programa25: Si compra un celular Huawei en Ripley
import os
#Detectores
cliente=" "
celular=" "

#INPUT vis OS
cliente=os.sys.argv[1]
celular=os.sys.argv[2]

#PROCESSING
#Si el celular es HUAWEI (tiene descuento más una mochila gratis)
if (celular=="Huawei"):
    print(cliente,"Tiene descuento más una mochila gratis")
#Si el celular no es LG (No tiene descuento)
if (celular=="LG"):
    print(cliente,"No tiene descuento")
#Si el celular es SAMSUNG (tiene solo descuento)
if (celular=="SAMSUNG"):
    print(cliente,"Tiene solo descuento")

#fin_if

