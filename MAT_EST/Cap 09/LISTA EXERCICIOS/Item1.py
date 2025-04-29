"""
Soma de Matrizes
Escreva  um  programa  em  Python  que  soma  duas  matrizes de mesmo  tamanho.  
As matrizes devem ser lidas como listas de listas e o resultado deve ser exibido na tela. Apresente a solução com e sem o uso do NumPy. 
Pratique suas habilidades de programação ao mesmo tempo que estuda Matemática.
"""

import numpy as np

def somaSemNumPy(matrizA, matrizB):
    #NÚMERO DE LINHAS
    num_linhas = len(matrizA)
    #NÚMERO DE COLUNAS
    num_colunas = len(matrizA[0])
    
    #MATRIZ RESULTANTE
    #matrizC = [[0 for j in range(num_colunas)] for i in range(num_linhas)]
    matrizC = [[0] * num_linhas for _ in range(num_colunas)]

    
    for i in range(num_linhas):
        j = 0
        for j in range(num_colunas):
            matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
    return matrizC


def somaComNumpy(matrizA, matrizB):
    matrizA = np.array(matrizA)
    matrizB = np.array(matrizB)
    matrizC = np.add(matrizA, matrizB)
    return matrizC
    

#START
matrizA = [[4, -1], [8, 3]]
matrizB = [[7, 9], [10, 6]]

somaSemNumPy(matrizA, matrizB)
print("Matriz A: ", matrizA)
print("Matriz B: ", matrizB)

print("\n\nSoma das Matrizes sem Numpy: ", somaSemNumPy(matrizA, matrizB))
print("Soma das Matrizes com NumPy: ", somaComNumpy(matrizA, matrizB))
#FIM