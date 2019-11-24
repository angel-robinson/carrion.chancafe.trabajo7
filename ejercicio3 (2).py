import os

#input
mi_nombre=os.sys.argv[1]

#validador de dato
mi_nombre_invalido=(mi_nombre!="eduardo")

while(mi_nombre_invalido):
    mi_nombre=input("ingrese mi nombre correcto:")
    mi_nombre_invalido=(mi_nombre!="eduardo")

#processing
for letra in mi_nombre:
    print(letra)

#fin_iterar
print("fin del bucle")

#ouput
print("minombre:",mi_nombre)

