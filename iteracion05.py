#decodificador mensaje inciptado
#cursos
#L=los cursos que llevo son:
#M=matematica
#P=programacion
#A=analisis matematico
#Q=quimica

import os

#imput
msg=os.sys.argv[1]

#inicio_iteracion
for letra in msg:
    if letra=="L":
        print("los cursos que llevo son:")
    if letra=="M":
        print("matematica")
    if letra=="P":
        print("programacion")
    if letra=="A":
        print("analis matematico")
    if letra=="Q":
        print("quimica")

#fin_iteracion
print("fin del bucle")
