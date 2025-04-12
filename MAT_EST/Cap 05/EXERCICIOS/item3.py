#Exercício 3: Norma de um Vetor
#Escreva uma função que calcule a norma (ou comprimento) de um vetor.

import numpy as np

def calNorma(A):
    return np.linalg.norm(A)

#START
A = [-5, 12, 0]
calNorma(A)
print("A norma do vetor A é: ", calNorma(A))
#END