# Crear un arreglo de dos dimensiones de 3 x 3 con números ceros,
# excepto la diagonal principal que debe contener en el mismo orden los siguientes elementos 1, 2 y 3.
'''
import numpy as np

matriz = np.zeros((3,3), dtype=int)
print(matriz)
contador = 1
for i in range(3):
    for j in range(3):
        if i == j:
            matriz[i][j] = contador
            contador = contador + 1
print(matriz)
'''
#Ejercicio 1 (Prácticos Semana 2)
# Crear dos arreglos de dos dimensiones de tamaño 3 x 3, con elementos de tipo numérico entero, luego:
# Muestra la matriz 1.
# Muestra la matriz 2.
# Muestre la matriz resultante de la multiplicación de la matriz 1 y matriz 2.

import numpy as np
import random as rd

matriz1 = np.diag([1,1,1])

for i in range(3):
    for j in range(3):
        matriz1[i][j] = rd.randint(0,100)
        
print(f"Matriz 1: \n {matriz1} ")

matriz2 = np.diag([1,1,1])

for i in range(3):
    for j in range(3):
        matriz2[i][j] = rd.randint(0,100)
        
print(f"Matriz 2: \n {matriz2} ")

matriz3 = matriz1 * matriz2
print(f"Matriz Multiplicada: \n {matriz3} ")