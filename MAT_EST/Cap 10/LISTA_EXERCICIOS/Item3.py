#Verifique se o determinante da matriz 3x3 abaixo é zero e se a matriz tem inversa.
import numpy as np

def calcDeterminante(matriz):
    det = np.linalg.det(matriz)
    return det

#START
dsa_matriz_3 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
determinante = calcDeterminante(dsa_matriz_3)
print(f"Determinante da matriz {dsa_matriz_3} é: {determinante}")

#Checando se a matriz tem inversa
if calcDeterminante(dsa_matriz_3) == 0:
    print("A matriz não tem inversa.")
else:
    print("A matriz tem inversa.")
#END