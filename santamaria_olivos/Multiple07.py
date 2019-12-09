#Programa27:Dado un número del 0 al 100
import os

#Declaración
num=0

#Input vis os
num=int(os.sys.argv[1])

#Processing
#Si es diferente a 0 (Es número es impar)
if (num%2 != 0):
    print("El número es impar")
#Si es igual a 0 (Es número par)
if (num%2==0):
    print("El número es par")
#Si el número es100 (Es un número muy alto)
if (num==100):
    print("Es un número muy alto")
#Si es mayor a 100 (Ingrese otro número)
if (num>100):
    print("Ingrese otro número")

#fin_if
