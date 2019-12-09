#Programa26: Simular compra de artículos
import os
#Detectores
cant_articulos=0

#INPUT vis OS
cant_articulos=int(os.sys.argv[1])

#PROCESSING
#Si los artículos comprados <3 (Pagar en efectivo)
if (cant_articulos < 3):
    print("Pagar en efectivo")
#Si los artículos comprados es >15 (Pagar en tarjeta)
if (cant_articulos>15):
    print("Pagar con tarjeta")
#Si los artículos comprados es 14 (Buena compra)
if (cant_articulos==20):
    print("Buena compra")
#Si los artículos comprados es 2 (Siga comprando)
if (cant_articulos>=2):
    print("Siga comprando")

#fin_if
