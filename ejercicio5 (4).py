import os
#imprimir la suma de los numeros menores a 15 y mayores a 10

#input
numero=int(os.sys.argv[1])
i=0

#validador de datos
numeros_no_permitidos=(numero<15 or numero>10)

while(numeros_no_permitidos):
    nuemro=int(input("ingrese un numero permitido:"))
    numeros_no_permitidos=(numero<15 or numero>10)

#processing
suma=0

while(i<=numero):
    suma +=i+1
    i +=1

#fin_while
print("la suma de los numeros es igual a :", suma)

#output
print("el numero es :",numero)
