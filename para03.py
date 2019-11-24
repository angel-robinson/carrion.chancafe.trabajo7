# Sumar los x numeros pares

import os

#input
x=int(os.sys.argv[1])
i=0
suma=0
while(i<=x):
    suma += i
    i += 2
#fin_while

print("La suma de los 10 primeros numeros pares:", suma)
