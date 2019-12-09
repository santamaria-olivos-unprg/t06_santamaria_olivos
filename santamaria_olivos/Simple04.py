#Programa4: Para calcular su promedio de matemáticas
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
#Si el promedio es mayo a 16
#Mostrar, tiene AD
if (promedio > 16):
    print(alumno,"tiene AD")

#fin_if
