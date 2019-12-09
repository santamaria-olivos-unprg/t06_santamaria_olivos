#Programa6: Simular compra de artículos
import os
#Detectores
cant_articulos=0

#INPUT vis OS
cant_articulos=int(os.sys.argv[1])

#PROCESSING
#Si los artículos comprados es menor a 3 Pagar en efectivo
#Mostrar, Pagar en efectivo
if (cant_articulos < 3):
    print("Pagar en efectivo")

#fin_if
