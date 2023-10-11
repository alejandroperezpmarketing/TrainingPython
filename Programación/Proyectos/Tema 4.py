##############Ejercicio 1#############




#nota = float(input("Introduce la nota"))
#nota<5 "Suspenso"
#7>nota>=5 "Aprobado"
#nota>=7 "Notable"
#9>nota>=7 "Sobresaliente"
#nota=10 "Matrícula de Honor"
#nota

nota = float(input("Introduce la nota"))
while nota !=10:
    if nota<5:
        print("Esta nota es un Suspenso")
    elif 7>nota>=5:
        print("Esta nota es un Aprobado")
    elif nota>=7:
        print("Esta nota es un Sobresaliente")
else:
    print("Esta nota es una Matrícula de Honor")