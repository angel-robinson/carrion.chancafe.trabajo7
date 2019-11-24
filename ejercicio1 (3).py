import os

#input
universidad=os.sys.argv[1]

#validador de dato
universidad_invalido=(universidad!="pedro ruiz gallo")

while(universidad_invalido):
    universidad=input("ingrese la universidad correcta:")
    universidad_invalido=(universidad!="pedro ruiz gallo")

#processing
for letra in universidad:
    print(letra)

#fin_iterar
print("fin del bucle")

#ouput
print("universidad:",universidad)
