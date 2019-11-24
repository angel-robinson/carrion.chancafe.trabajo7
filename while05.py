import os
#imprimir si ingresa la cantidad de polos si es igual a 1
polos=int(os.sys.argv[1])
invalido=True

while(invalido):
    print("##################################")
    print("Ingrese la cantidad de productos:",polos)
    print("##################################")
    invalido=(polos !=1)
    if (polos == True):
        print("## error ##")
    else :
        print("# es,correcto")
#fin_bucle
print("fin del bucle")
