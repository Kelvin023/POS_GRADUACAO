"""
Exercício 2: Multiplicação de Matrizes
Implemente  uma  função  em  Python  que  multiplica  duas  matrizes.  Verifique  se  as dimensões  das  matrizes  são  compatíveis  para  a  multiplicação  e  
retorne  a  matriz  resultante. Apresente a solução com e sem o uso do NumPy. Pratique suas habilidades de programação ao mesmo tempo que estuda Matemática
"""

import numpy as np

def verificaCompatibilidade(matrizA, matrizB):
    # Verifica se o número de colunas da matriz A é igual ao número de linhas da matriz B
    if len(matrizA) != len(matrizB[0]):
        raise ValueError("AS DIMENSÕES DAS MATRIZES NÃO SÃO COMPATÍVEIS PARA MULTIPLICAÇÃO.")
    
def multComNumPy(matrizA, matrizB):
    matrizA = np.array(matrizA)
    matrizB = np.array(matrizB)
    matrizC = np.dot(matrizA, matrizB)
    return matrizC

#START
matrizA = [[0, 7], [-9, 3]]
matrizB = [[4, 2], [5, -3]]

try:
    verificaCompatibilidade(matrizA, matrizB)
    print("As matrizes são compatíveis para multiplicação.")
    multComNumPy(matrizA, matrizB)
    print("Matriz A: ", matrizA)
    print("Matriz B: ", matrizB)
    print("\n\nMultiplicação das Matrizes com NumPy: ", multComNumPy(matrizA, matrizB))    
except ValueError as e:
    print(f"Erro: {e}")
#END