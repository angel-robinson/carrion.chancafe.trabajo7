# Decodificar mensaje encriptado
# x = ¿donde estas?
# y = ¿nos podemos ver?
# z = en el lugar de siempre
# t = ven rapido por favor

import os
#input
msg=os.sys.argv[1]

#bucle
for letra in msg:
    if letra == "X":
        print("¿donde estas?")
    if letra == "Y":
        print("¿nos podemos ver?")
    if letra == "Z":
        print("en el lugar de siempre")
    if letra == "T":
        print("ven rapido por favor")
#fin_iterador

print("Fin del bucle")
