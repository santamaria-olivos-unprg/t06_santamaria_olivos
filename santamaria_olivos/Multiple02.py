#Programa22: Dado el número de rifa
import os

#Declaración
nombre=" "
num_rifa=0

#INPUT vis OS
nombre=os.sys.argv[1]
num_rifa=int(os.sys.argv[2])

#PROCESSING
#Si el número es menor a 348 (Casi te llaves un premio)
if ( num_rifa <348 ):
    print(nombre,"Casi te llevas un premio")
#Si el número es 348 (Ganaste un TV LG!)
if ( num_rifa==348 ):
    print(nombre,"Ganaste un TV LG!!")
#Si el número es 349 (Ganaste un premio sorpresa)
if ( num_rifa==349):
    print(nombre,"Ganaste un premio sorpresa")
#Si el número es 350 (Ganaste una licuadora)
if ( num_rifa==350):
    print(nombre,"Ganaste una licuadora")
#Si el número es 351 (Ganaste un celular)
if ( num_rifa==351):
    print(nombre,"Ganaste un celular")
#Si el número es > 351 (Sigue intentando)
if (num_rifa > 351):
    print(nombre,"Sigue intentando")

#fin_if
