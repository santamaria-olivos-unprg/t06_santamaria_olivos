# Programa 05

import os

#Declaracion
apellido,nro_medallas="",0


#INPUT

apellido=str(os.sys.argv[1])
nro_medallas=int(os.sys.argv[2])

#PROCESSING
#Si el numero de medallas es mayor que 5
#mostrar "Participas el proximo año!!"
participa_prox_año=( nro_medallas >= 5)

if ( nro_medallas >= 5):
    print(apellido, "Participas el proximo año!!")
