# Sumar los x numeros desde 0

import os

#input
q=int(os.sys.argv[1])
i=0

suma=0
while(i<=q):
    suma += i
    i += 1
#fin_while

print("La suma de los 10 primeros numeros:", suma)
