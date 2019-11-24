#la suma de los numeros que hay entre m y n
import os

#input
m=int(os.sys.argv[1])
n=int(os.sys.argv[2])
i=m
suma=0

while(i<=n):
    suma+=i
    i+=1
#fin_while
print("la suma de los numeros que hay entre 5 y 10:",suma)
