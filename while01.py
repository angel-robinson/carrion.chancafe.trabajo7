import os
#DECLARAR VARIABLES
base,altura=0,0
area=0
#imput
base=int(os.sys.argv[1])
altura=int(os.sys.argv[2])

#procesing
area_invalida=(base*altura/2)

#Verificador
area=(area < 0 or area > 50 )

#validar el area de un triangulo
area_invalida=True
while (area_invalida):
    area=int(input("ingrese el area:"))
    area_invalida=(area < 0 or area > 50  )
#fin_while
print("fin del bucle")
