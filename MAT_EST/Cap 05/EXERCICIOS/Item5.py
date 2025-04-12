#Exercício 5: Projeção de um Vetor sobre Outro
#Escreva uma função que encontre a projeção de um vetor sobre outro vetor


import numpy as np

def projecaoVetores(v, u):
    P = (np.dot(v,u) / np.dot(u,u)) * u
    return P

#START
v = np.array([3,1])
u = np.array([1,1])
projecao = projecaoVetores(v,u)
print(f"A projeção do vetor {v} sobre o vetor {u} é: {projecao}")
#FIM