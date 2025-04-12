#Exercício 1: Soma de Vetores
# Escreva  uma  função  em  Python  que  some  dois  vetores.  Suponha  que  os vetores  têm  o  mesmo  tamanho.  
# Resolva  o  exercício  de  forma  diferente  do  que  foi mostrado nas aulas.

import numpy as np

def soma_vetores(vetor1, vetor2):
    """Soma dois vetores de mesmo tamanho."""
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho.")
    
    return np.add(vetor1, vetor2)

# Exemplo de uso
vetor1 = np.array([1, 2, 3])
vetor2 = np.array([4, 5, 6])
resultado = soma_vetores(vetor1, vetor2)
print("Resultado da soma dos vetores:", resultado)