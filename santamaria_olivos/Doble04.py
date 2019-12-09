#Programa14: Para calcular si promedio de matemáticas es AD
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
#Mostrar, tiene que estudiar más
if (promedio > 16):
    print(alumno,"felicitaciones tienes AD")
else:
    print(alumno,"tiene que estudiar más")

#fin_if
