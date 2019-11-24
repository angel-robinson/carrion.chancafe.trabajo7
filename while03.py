#velocidad angular
import os
#declaracion de variables
acceleracion,radio=0,0

#imput
acceleracion=int(os.sys.argv[1])
radio=int(os.sys.argv[2])


#procesing
velocidad_angular=(acceleracion*radio)

#Verificador
velocidad_angular=(velocidad_angular< 0 or velocidad_angular > 50 )

#validar la velocidad angular
velocidad_angular_invalida=True
while (velocidad_angular_invalida):
    velocidad_angular=int(input("ingrese velocidad angular:"))
    velocidad_angular_invalida=(velocidad_angular < 0 or velocidad_angular > 50)
#fin_while
print("fin del bucle")
