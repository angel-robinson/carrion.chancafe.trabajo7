import os
#mostrar error si no ingresa el codigo 1234
codigo=os.sys.argv[1]
invalido=True

while(invalido):
    print("##################################")
    print("Ingrese el codigo por favor:",codigo)
    print("##################################")
    invalido=(codigo!=1234)
    if (invalido == True):
        print("## lo sentimos;error ##")
    else :
        print("# es correcto")
#fin_bucle
print("fin del bucle")
