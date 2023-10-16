import pandas as pd
import random
import numpy as np


###################EJERCICIOS TEMA 4######################################

#########################ejerciciop 5#############

####definir varios funciones en cadena###########
#funcion 1
#mostrar True si el valor entero 1 es  divisible entre el valor entero 2 y Falso si lo contrario

#inputs
def recolectar_inputs():
    while True:
        try:
            valor_entero = int(input("Escribe el valor aquí en número enteros:"))
            break
        except (ValueError, TypeError):
            print("Introduce un valor entero")
    return valor_entero
    """
    while True:
        try:    
            global valor_entero2
            valor_entero2 = int(input("Escribe el valor 2 aquí en número enteros:"))
            break
        except (ValueError, TypeError):
            print("Introduce un valor entero 2")
"""

def recolectar_inputs_1_2():
    global Valor_1
    #Valor_1 = recolectar_inputs()
    print("Valor1:")
    Valor_1 = recolectar_inputs()
    global Valor_2
    print("Valor2:")
    Valor_2 = recolectar_inputs()
    return Valor_1, Valor_2


def true_or_false_division_entre_numeros_divisible_o_no():
    recolectar_inputs_1_2()
    if Valor_1%Valor_2 == 0:
        print(True,":","El primer número es divisible por el segundo")
    else:
        print(False,":","El primer número no es divisible por el segundo")

valor1, Valor_2 = recolectar_inputs_1_2()
true_or_false_division_entre_numeros_divisible_o_no()

"""
def main_function():
    recolectar_inputs_1_2()
    true_or_false_division_entre_numeros_divisible_o_no(Valor_1,Valor_2)

"""
##########funcion 2   sumar  todos los datos con ls que se pueda  dividir un valor#########
#intentar desde el 1 hasta que sea verdadero menos el valor - si un vlor es divisible por n
#adjuntarlo a la lista, sino dar un print("La suma de los valores divisibles de este numero es:")


def calculo_de_suma_de_divisibles():
    global valores_divisibles
    valores_divisibles = []
    n = 1
    recolectar_inputs_1_2()
    while True:
        try:
            for n in range(n,(valor1-1)):
                    if Valor_1%n == 0:
                        valores_divisibles.append(n)
                        n = n+1
                    else:
                        n = n+1
                        #print("sorry")
                        pass
        finally:
            suma_de_valores_divisibles = sum(valores_divisibles)    
            print_value = print("La suma de los valores divisibles es:",suma_de_valores_divisibles)
            return valores_divisibles



calculo_de_suma_de_divisibles()
