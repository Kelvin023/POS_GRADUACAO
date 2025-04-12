#Crie um programa que encontra as raízes de uma equação quadrática do tipo ax^2 + bx + c = 0. 
# O programa deve lidar com todos os tipos de raízes (reais e complexas).

import math

#Calculando o valor de Delta
def calcDelta (a, b, c):
    return ((b**2) - (4*a*c))

def calcBaskara (b, delta, a):
    if Delta > 0:
        print(f"Valor de a: {a}")
        print(f"Valor de b: {b}")
        print(f"Valor de delta: {delta}")
        print("\nEquação possui duas soluções reais")
        print(f"X1 = {(-1*b + (delta ** 0.5))/(2*a)}")
        print(f"X2 = {(-1*b - (delta ** 0.5))/(2*a)}")                
    elif Delta == 0:
        print("\nEquação possui uma solução real")
        print(f"X1 = {(-1*b) / 2 *a}")
    else:
        print("\nEquação não possui uma solução real")
    


valorA = float(input("Informe o valor de a: "))
valorB = float(input("Informe o valor de b: "))
valorC = float(input("Informe o valor de c: "))

print(f"Valor de Delta: {calcDelta(valorA, valorB, valorC)}")
Delta = float(calcDelta(valorA, valorB, valorC))
#print(f"DELTA = {Delta}")

calcBaskara(valorB, Delta, valorA)