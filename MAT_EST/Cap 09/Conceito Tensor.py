#Os tensores são como vetores e matrizes, mas podem ter n dimensões. Por exemplo, para criar um tensor 3x3x2x1, olha só o exemplo abaixo:

import numpy as np

#START
t = np.array([[[[1],[2]],[[3],[4]],[[5],[6]]], [[[7],[8]],[[9],[10]],[[11],[12]]], [[[13],[14]],[[15],[16]],[[17],[18]]]])
print(t)
print("Shape do tensor: ", [t.shape]) #mostra a forma do tensor, ou seja, quantas dimensões ele tem e o tamanho de cada dimensão

#Funçao pra transforma um tensor em um vetor
vetor_flatten = t.flatten()
print("Vetor Flatten: ", vetor_flatten) #mostra o vetor transformado em um vetor 1D, ou seja, com apenas uma dimensão

#Funcao para converter em vetor usando ravel
vetor_ravel = t.ravel()
print("Tipo do elemento: ", type(vetor_ravel)) #mostra o tipo do vetor, que é um array numpy
print("Vetor usando Ravel: ", vetor_ravel) #mostra o vetor transformado em um vetor 1D, ou seja, com apenas uma dimensão


#E se eu quiser converter em Matriz? Olha só:
matriz = t.reshape(6, 3) #transforma o tensor em uma matriz 6x3
print("\nMatriz 6x3: \n", matriz) #mostra a matriz transformada

#Olha só a matriz em outro formato 3x6:
matriz2 = t.reshape(3, 6) #transforma o tensor em uma matriz 3x6
print("\nMatriz 3x6: \n", matriz2) #mostra a matriz transformada
#END