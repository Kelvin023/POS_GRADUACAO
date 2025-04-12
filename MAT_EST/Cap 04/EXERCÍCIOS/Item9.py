#Escreva um script que calcula o logaritmo de base 10 de um número fornecido pelo usuário. Certifique-se de tratar o caso em que o logaritmo não pode ser definido (números negativos e zero).
#se o parametro do logaritmo for numero negativo ou zero, entao pode printar queste valor nao existe, nao esta definido

import math as mt
import numpy as np

def f(x):
    if x < 0:
        print("INDEFINIDO! Foi informado um valor negativo")
    elif x == 0:
        print("INDEFINIDO! Foi informado o valor ZERO")
    else:
        return np.log10(x)

#START
x = int(input("Entre com um número para calcularmos o logaritmo desse cara: "))
y = f(x)

print(round(y,5))#usei esse round só pra deixar arredondado pra 5 casas depois da vírgula