import os

#input
nombre_de_mi_mama=os.sys.argv[1]

#validador de dato
nombre_de_mi_mama_invalido=(nombre_de_mi_mama!="rosa")

while(nombre_de_mi_mama_invalido):
    nombre_de_mi_mama=input("ingrese el nombre de mi mama correcto:")
    nombre_de_mi_mama_invalido=(nombre_de_mi_mama!="rosa")

#processing
for letra in nombre_de_mi_mama:
    print(letra)

#fin_iterar
print("fin del bucle")

#ouput
print("nombredemimama:",nombre_de_mi_mama)
