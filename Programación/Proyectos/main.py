import pandas as pd
##############PARTE 1#####################
import random
def genera_lista_aleatoria(longitud, inicio, fin):
    lista=[]
    i=0
    while i<longitud:
        num=random.randint(inicio, fin)
        if num not in lista:
            lista.append(num)
            i+=1
    return lista


###########Ejercicio 4#################
genera_lista_aleatoria(20, 1, 100)


###########Ejercicio 5#################

lista_de_10_ejer4 = genera_lista_aleatoria(10, 1, 20)
print(lista_de_10_ejer4)
new_lista_de_10_ejer4 = []
def valor_alcuadrado():
    for n in lista_de_10_ejer4:
        new_n = n**2
        new_lista_de_10_ejer4.append(new_n)
    return new_lista_de_10_ejer4

print(valor_alcuadrado())

###########Ejercicio 6#################
texto = """Menos tu vientre, todo es confuso. Menos tu vientre, todo es futuro fugaz, pasado baldío, turbio. Menos tu vientre, todo es oculto."""
print(len(texto))
###########Ejercicio 7#################

#######calculo del DNI############
letras = { 0:"T",
           1:"R",
           2:"W",
           3:"A",
           4:"G",
           5:"M",
           6:"Y",
           7:"F",
           8:"P",
           9:"D",
           10:"X",
           11:"B",
           12:"N",
           13:"J",
           14:"Z",
           15:"S",
           16:"Q",
           17:"V",
           18:"H",
           19:"L",
           20:"C",
           21:"K",
           22:"E"
}

print(letras.keys())

###
numero_de_dni = int(input("Escribe el DIN  sin letra"))
resto_valor = numero_de_dni%23
print(resto_valor)
print(letras[resto_valor])

###########Ejercicio 8#################

