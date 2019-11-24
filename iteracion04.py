#decodificar mensaje incriptado
#integrantes de mi familia
#M=los integrantes de mi familia son:
#F=franklin carrion
#C=carmen rosa cruz
#G=gryshi carrion
#A=angel carrion
#L=luzbany carrion

import os

#inicio_iteracion
#input
msg=os.sys.argv[1]
for numero in msg:
     if numero=="M":
         print("los integrantes de de mi famila son:")
     if numero=="F":
         print("franklin carrion")
     if numero=="C":
         print("carmen rosa cruz")
     if numero=="G":
         print("gryshi carrion")
     if numero=="A":
         print("angel carrion")
     if numero=="L":
         print("luzbany carrion")
#fin_iteracion
print("fin del bucle")
