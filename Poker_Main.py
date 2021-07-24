# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 16:50:55 2021

@author: setv9
"""

import random

# Numeros correspondientes a las cartas
# - El 1 == A o equivalente a 14
# - El 11 = J, 12 = Q y 13 = K
# - C = corazones rojos, T = Trébol, D = Diamante, N = Corazones negros
numeros = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
palos = ["C","T","D","N"]

# Formación de las 52 cartas, una lista formada por tuplas
cartas = []

for n in numeros:
    for p in palos:
        cartas.append((n,p))

print("Cartas:\n", cartas)

# Código para barajar las cartas
cartas_barajadas = random.sample(cartas, k = len(cartas))
print("Cartas barajadas:\n", cartas_barajadas)

def poker_clasico():
    num_jugadores = int(input("Ingresa el número de jugadores (Mínimo 2, Máximo 9): "))
    if num_jugadores < 2 and num_jugadores >9:
        print("Número de jugadores no válido")

opcion = ""
while opcion != "0":
    print("1- Póker clásico")
    print("2- Texas Hold-em")
    print("3- Omaha hi/lo")
    print("0- Salir")
    opcion = input("Escoja el tipo de juego: ")
    
    if opcion == "1":
        poker_clasico()


