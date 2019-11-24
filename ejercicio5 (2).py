import os

#input
notas_musicales=os.sys.argv[1]

#validador de dato
notas_musicales_invalido=(notas_musicales!="do re mi fa sol la si")

while(notas_musicales_invalido):
    notas_musicales=("ingrese las notas musicales correctas")
    notas_musicales_invalido=(notas_musicales!="do re mi fa sol la si")

#processing
for letra in notas_musicales:
    print(letra)

#fin_iterar
print("fin del bucle")

#ouput
print("notasmusicales:",notas_musicales)
