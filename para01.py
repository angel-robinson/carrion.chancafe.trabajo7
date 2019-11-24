# Sumar los x numeros desde 50

import os

#input
q=int(os.sys.argv[1])
i=50

suma=0
while(i<=q):
    suma += i
    i += 1
#fin_while

print("La suma de los 100 primeros numeros despues de 50 es:", suma)
