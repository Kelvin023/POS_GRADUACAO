#Exercício 4: Comparando Distâncias
#Escreva  um  script  que  receba  três  vetores  de  mesma  dimensão.  Calcule  a distância  euclidiana  entre  o  primeiro  e  os  outros  dois  vetores.  
#Imprima  qual  dos  dois vetores está mais próximo do primeiro, baseado na distância euclidiana


import numpy as np
import math

def calcDistEuclid(vet1, vet2):
    if len(vet1) != len(vet2):
        raise ValueError("Os vetores devem ter a mesma dimensão")
    
    soma = sum((a - b) ** 2 for a, b in zip(vet1, vet2))
    return math.sqrt(soma) 


#START
vetor1 = [1, 2, 3]
vetor2 = [5, 7.0, 1/6]
vetor3 = [1.4, 0.33, 2.2]

distEuc2 = calcDistEuclid(vetor1, vetor2)
distEuc3 = calcDistEuclid(vetor1, vetor3)

if distEuc2 < distEuc3:
    print(f"O vetor 2 está mais próximo do vetor 1 com distância {distEuc2}")
else:
    print(f"O vetor 3 está mais próximo do vetor 1 com distância {distEuc3}")
#FIM