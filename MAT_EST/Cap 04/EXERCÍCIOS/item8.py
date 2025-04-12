#Para a equação quadrática ax^2 + bx + c = 0, calcule o discriminante e determine o número de raízes reais.
import math

#Calculando o valor do Discriminante
def calcDiscriminante (a, b, c):
    return ((b**2) - (4*a*c))

def calcBaskara (b, discriminante, a):
    if discriminante > 0:   
        print("\nEquação possui duas soluções reais")
        print(f"X1 = {(-1*b + (discriminante ** 0.5))/(2*a)}")
        print(f"X2 = {(-1*b - (discriminante ** 0.5))/(2*a)}")                
    elif discriminante == 0:
        print("\nEquação possui uma solução real")
        print(f"X1 = {(-1*b) / 2 *a}")
    else:
        print("\nEquação não possui uma solução real")
    

#START
valorA = float(input("Informe o valor de a: "))
valorB = float(input("Informe o valor de b: "))
valorC = float(input("Informe o valor de c: "))

Discriminante = float(calcDiscriminante(valorA, valorB, valorC))
print(f"DISCRIMINANTE = {Discriminante}")
calcBaskara(valorB, Discriminante, valorA)