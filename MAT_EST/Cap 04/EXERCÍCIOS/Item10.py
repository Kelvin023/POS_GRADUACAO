#Utilize logaritmo para calcular o tempo necessário para que um investimento atinja um determinado valor, considerando uma taxa de crescimento contínua.

import math as mt
import numpy as np


def f(m,c,r):
    return ((np.log(m) - np.log(c)) / r)


#START
c = float(input("Informe o capital inicial: "))
m = float(input("Informe o valor futuro(esperado): "))
r = float(input("Informe a taxa de juros correspondente: "))

t = f(m,c,r)
if t < 2:
    print(f"O tempo necessário para o atingimento do valor é: {round(t,2)} ano")
else:
    print(f"O tempo necessário para o atingimento do valor é: {round(t,2)} anos")