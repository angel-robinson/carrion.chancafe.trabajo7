#la suma de los numeros que hay entre x e y
import os

#input
nota1=int(os.sys.argv[1])
nota2=int(os.sys.argv[2])
promedio=(nota1+nota2)/2
i=promedio
suma=0

while(i<=promedio):
    suma+=i
    i+=1
#fin_while
print("el promedio que hay entre la nota1 y la nota2 es:",suma)
