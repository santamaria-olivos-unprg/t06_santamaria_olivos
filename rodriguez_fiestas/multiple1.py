# Programa 21

# Programa para calcular 3 notas de matematica
import os
#Declaración de variables
n1,n2,n3=0,0,0

#INPUT VIA OS
n1=int(os.sys.argv[1])
n2=int(os.sys.argv[2])
n3=int(os.sys.argv[3])

#PROCESSING
prom=int((n1+n2+n3)/3)

#Condicion multiple
#Si el prom=>16 y 20 (A)
if (prom >= 16 and prom <= 20):
    print("A")
#Si el prom 11 y 15 (B)
if (prom >= 11 and prom <= 15):
    print("B")
#Si el prom 0 y 10 (C)
if (prom >= 0 and prom <= 10):
    print("C")

#fin_if
