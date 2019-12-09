#Programa11 para calcular el sobre peso
import os

#Declaración
paciente=" "
altura=0.0
peso=0.0
masa_corporal=0.0

#INPUT vis OS
paciente=os.sys.argv[1]
altura=float(os.sys.argv[2])
peso=int(os.sys.argv[3])


#PROCESSING
masa_corporal=(peso/altura)
#Si el resultado es mayor a 25.0
#Mostrar, Tiene sobre peso
#Mostrar No tiene sobre peso
if (masa_corporal >= 25):
    print("El paciente",paciente,"tiene sobre peso")
else:
    print("El paciente",paciente,"no tiene sobre peso")

#fin_if
