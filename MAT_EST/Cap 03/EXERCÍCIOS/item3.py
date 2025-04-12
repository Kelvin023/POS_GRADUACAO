#Faça um programa que resolve uma equação linear do tipo ax + b = 0. Os valores de a e b são fornecidos pelo usuário.

import math

valorA = float(input("Entre com o valor de a: "))
valorB = float(input("Entre com o valor de b: "))

if valorA == 0:
    print("Sem solução! Valor de A igual a zero.")
    exit()

valorFinal = ((-1 * valorB) / valorA)
print(f"Valor final de X = {valorFinal}")