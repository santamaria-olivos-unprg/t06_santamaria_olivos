#Programa30: Calcule el total a pagar por la compra de zapatillas
import  os

#Declaraciones
cantidad=0
costo=0.0
descuento=0.0
precio_original=0.0
precio_final=0.0

#Input vis os
cantidad=int(os.sys.argv[1])
precio_original=int(os.sys.argv[1])
#Processing
costo=cantidad*precio_original
descuento=costo*0.1
precio_final=costo-descuento

#Si compras 2 pares de zapatillas (Tiene 10% de descuento)
if (cantidad==2 ):
    print("El precio final es",precio_final)
#Si compras 1 par de zapatillas (No tienes descuento)
if (cantidad==1):
    print("El precio final es",costo)
#Si compra mas de 2 pares de zapatillas (Tienes 20% de descuento)
if (cantidad>2):
    descuento=costo*0.2
    print("El precio final es",precio_final)

#fin_if
