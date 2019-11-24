# Decodificar mensaje encriptado
# A = Hola
# B = ¿como estas?
# C = Me alegra verte
# D = Espero verte pronto
import os
#input
msg=os.sys.argv[1]

#inicio_iterador
for letra in msg:
    if letra == "A":
        print("Hola")
    if letra == "B":
        print("¿Como estas?")
    if letra == "C":
        print("me alegra verte")
    if letra == "D":
        print("espero verte pronto")
#fin_iterador

print("Fin del bucle")
