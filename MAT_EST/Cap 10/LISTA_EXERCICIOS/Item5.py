#Calcule o determinante e a inversa da matriz 4x4 abaixo, caso a inversa exista.
import numpy as np

def calcDeterminante(matriz):
    det = np.linalg.det(matriz)
    return det

def calcInversa(matriz):
    inversa = np.linalg.inv(matriz)
    return inversa

#START
matriz = [[1, 0, 2, -1], [3, 0, 0, 5], [2, 1, 4, -3], [1, 0, 5, 0]]
determinante = calcDeterminante(matriz)
print(f"Determinante da matriz {matriz} é: {determinante}")

if determinante != 0:
    inversa = calcInversa(matriz)
    print(f"Inversa da matriz é: \n{inversa}")
else:
    print("A matriz não é inversível.")
#END