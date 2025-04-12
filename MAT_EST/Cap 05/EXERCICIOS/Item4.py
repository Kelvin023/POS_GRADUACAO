#Exercício 4: Ângulo entre Dois Vetores
#Implemente uma função que calcule o ângulo (em graus) entre dois vetores

import numpy as np
import math

def angle_between_vectors(v1, v2):
    #Calcula o ângulo entre dois vetores em graus.
    #Calcula o produto escalar dos vetores
    dot_product = np.dot(v1, v2)
    
    # Calcula as normas (módulos) dos vetores
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    # Calcula o cosseno do ângulo
    cos_angle = dot_product / (norm_v1 * norm_v2)
    
    # Calcula o ângulo em radianos e depois converte para graus
    angle_rad = np.arccos(cos_angle)
    angle_deg = np.degrees(angle_rad)
    
    return angle_deg

# Testando a função
v1 = np.array([1, 0])
v2 = np.array([0, 1])
angle = angle_between_vectors(v1, v2)
print(f"O ângulo entre os vetores {v1} e {v2} é {angle:.2f} graus.")