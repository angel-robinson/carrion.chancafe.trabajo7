#decodificador mensaje incriptado
#nombre y apellidos
#I=mis nombres y apellidos son:
#A=angel
#B=robinson
#C=carrion
#D=cruz

import os
#input
msg=os.sys.argv[1]
#inicio_iterador
for letra in msg:
    if letra=="I":
        print("mi nombre y apellido es:")
    if letra=="A":
        print("angel")
    if letra=="B":
        print("robinson")
    if letra=="C":
        print("carrion")
    if letra=="D":
        print("cruz")
#fin_iterador
print("fin del bucle")


