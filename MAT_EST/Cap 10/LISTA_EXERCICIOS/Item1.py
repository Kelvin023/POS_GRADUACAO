"""
Calcule o determinante da matriz 3x3 abaixo.
"""

import numpy as np

def calDeterminante(dsa_matriz_1):
    # Calcular o determinante da matriz 3x3
    det = np.linalg.det(dsa_matriz_1)
    return det


#START
dsa_matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Determinante da matriz {dsa_matriz_1} é: {calDeterminante(dsa_matriz_1)}")
#END