#Programa21: para calcular el sobre peso
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
#Si el resultado de masa corporal>=18.5 y 24.9 (Tiene peso normal)
if (masa_corporal>=18.5 and masa_corporal<=24.9 ):
    print("El paciente",paciente,"tiene peso normal")
#Si el resultado de masa corporal>=18.5 y 24.9 (Tiene sobre peso)
if (masa_corporal >=25 and masa_corporal <= 29.9 ):
    print("El paciente",paciente,"tiene sobre peso")
#Si el resultado es mayor a 30 (Tiene obesidad)
if (masa_corporal > 30):
    print("El paciente",paciente,"tiene obesidad")

#fin_if
