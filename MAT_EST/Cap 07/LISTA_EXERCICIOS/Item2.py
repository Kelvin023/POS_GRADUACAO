#Exercício 2: Distância Euclidiana com Validação de Dados
#Modifique a função do Exercício 1 para validar se os dois vetores têm o mesmo tamanho. Se não tiverem, a função deve retornar um erro

#Exercício 1: Cálculo de Distância Euclidiana
#Escreva uma função em Python que receba dois vetores (listas de números) de mesma dimensão e retorne a distância euclidiana entre eles

import math

def distancia_euclidiana(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter a mesma dimensão")

    soma = sum((a - b) ** 2 for a, b in zip(vetor1, vetor2))
    return math.sqrt(soma)

# Exemplo de uso:
vetor_a = [1, 2]#pra causar o erro propositalmente mesmo
vetor_b = [4, 5, 6]

resultado = distancia_euclidiana(vetor_a, vetor_b)
print(f"A distância euclidiana é: {resultado}")