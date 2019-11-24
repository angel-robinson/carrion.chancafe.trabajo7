import os
#imprimir la suma de los impares de los numeros entre [10,12]

#input
numero=int(os.sys.argv[1])
i=0

#validador de datos
numeros_no_permitidos=(numero<10 or numero>12)

while(numeros_no_permitidos):
    numero=int(input("ingresar un numero permitido:"))
    numeros_no_permitidos=(numero<10 or numero>20)

#processing
suma_impares=0

while(i<=numero):
    suma_impares +=i+2
    i +=2

#fin_while
print("la suma de los impares es igual a :",suma_impares)

#output
print("el numero es :",numero)
