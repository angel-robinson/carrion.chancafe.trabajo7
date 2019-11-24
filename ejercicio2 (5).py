import os
#imprimir la suma de los pares de los numeros entre [5,10]

#input
numero=int(os.sys.argv[1])
i=0

#validador de los datos
numeros_no_permitidos=(numero<5 or numero>10)

while(numeros_no_permitidos):
    numero=int(input("ingresar un numero permitido:"))
    numeros_no_permitidos=(numero<5 or numero>10)

#processing
suma_pares=0

while(i<=numero):
    suma_pares +=i+2
    i +=2

#fin_while
print("la suma de los pares es igual a :",suma_pares)

#output
print("el numero es :",numero)






