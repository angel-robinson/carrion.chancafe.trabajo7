import os

#input
curso=os.sys.argv[1]

#validador de dato
curso_invalido=(curso!="programacion")

while(curso_invalido):
    curso=input("ingrese el curso correcto:")
    curso_invalido=(curso!="programacion")


#porcessing
for letra in curso:
    print(letra)

#fin_iterar
print("fin del bucle")

#ouput
print("curso:", curso)
