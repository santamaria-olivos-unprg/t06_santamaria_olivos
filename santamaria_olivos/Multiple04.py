#Programa24: Para calcular si promedio de matemáticas es AD
import os

#Declaración
alumno=" "
nota1=0.0

#INPUT vis OS
alumno=os.sys.argv[1]
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])

#PROCESSING
promedio=(nota1+nota2+nota3)/3
#Si el promedio es <=10 (Tiene C)
if (promedio<=10):
    print(alumno,"tiene C")
#Si el promedio es <10 y 13 (Tiene B)
if (promedio>10 and promedio<=13):
    print(alumno,"tiene B")
#Si el promedio es <13 y 16 (Tiene A)
if (promedio>13 and promedio<=16):
    print(alumno,"tiene A")
#Si el promedio es <17 y 20 (Tiene AD)
if (promedio>16 and promedio==20):
    print(alumno,"tiene AD")

#fin_if
