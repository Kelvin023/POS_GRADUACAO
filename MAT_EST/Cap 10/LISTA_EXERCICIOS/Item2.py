#Crie uma função em Python que receba uma matriz 2x2 e retorne sua inversa. Não use o NumPy. Teste sua função com a seguinte matriz:

import numpy as np

def isQuadrada(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    return True

def calcDeterminante(matriz):
    det = np.linalg.det(matriz)
    return det

def calcInversa(dsa_matriz_2, det):
    # Calcular a inversa da matriz 2x2
    inversa = [[dsa_matriz_2[1][1] / det, -dsa_matriz_2[0][1] / det],
               [-dsa_matriz_2[1][0] / det, dsa_matriz_2[0][0] / det]]
    return inversa


#START
dsa_matriz_2 = [[4, 7], [2, 6]]

#Verifica se a matriz é quadrada
if not isQuadrada(dsa_matriz_2):
    raise ValueError("A matriz não é quadrada.")
#Verifica se o determinante é diferente de zero
if calcDeterminante(dsa_matriz_2) == 0:
    raise ValueError("A matriz não é inversível.")
else:
    determinante = calcDeterminante(dsa_matriz_2)        
    print(f"Determinante da matriz {dsa_matriz_2} é: {determinante}")    
    
inversa = calcInversa(dsa_matriz_2, determinante)
print(f"Inversa da matriz {dsa_matriz_2} é: {inversa}")
#END