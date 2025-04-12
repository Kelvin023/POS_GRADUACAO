#Exercício 2: Produto Escalar
#Implemente  uma  função  que  calcule  o  produto  escalar  entre  dois  vetores. 
#Resolva o exercício de forma diferente do que foi mostrado nas aulas


import numpy as np

def produtoEscalar(A,B):
    soma = 0
    for i in range(len(A)):
        soma += A[i] * B[i]
    return soma


#START
A = [1,3,-5]
B = [4,-2,-1]

print("O produto escalar entre A e B é: ", produtoEscalar(A,B))