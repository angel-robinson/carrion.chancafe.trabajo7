import os
#imprimir si ingresa la cantidad de productos si es igual a 5
cantidad=int(os.sys.argv[1])
invalido=True

#inicio_while
while(invalido):
    print("##################################")
    print("Ingrese la cantidad de productos:",cantidad)
    print("##################################")
    invalido=(cantidad !=5)
    if (invalido == True):
        print("## error ##")
    else :
        print("# es,correcto")
#fin_while

print("fin del bucle")


