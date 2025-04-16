#Exercício 3: Distância Euclidiana em N-Dimensões
#Generalize  a  função  do  Exercício  1  para  que  ela  possa  calcular  a  distância euclidiana entre dois vetores em um espaço de 
#qualquer número de dimensões
###?????????????????????????????????????????????????????????????????
import math

def distancia_euclidiana(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter a mesma dimensão")

    soma = sum((a - b) ** 2 for a, b in zip(vetor1, vetor2))
    return math.sqrt(soma)

# Exemplo de uso:
vetor_a = [1, 2, 3, 4]
vetor_b = [5, 6, 7, 8]

resultado = distancia_euclidiana(vetor_a, vetor_b)
print(f"A distância euclidiana é: {resultado}")