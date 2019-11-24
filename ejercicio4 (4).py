import os
#imprimir la suma de los cubos de los numeros del intervalo [2,4]

#input
numero=int(os.sys.argv[1])
i=0

#validador de datos
intervalo_no_permitido=(numero<2 or numero>4)

while(intervalo_no_permitido):
    numero=int(input("ingresar un numero del intervalo permitido:"))
    intervalo_no_permitido=(numero<2 or numero>4)

#processing
suma_cubos=0

while(i<=numero):
    suma_cubos +=i**3
    i +=1

#fin_while
print("la suma de los cubos es igual a: ",suma_cubos)

#output
print("el numero es :", numero)
