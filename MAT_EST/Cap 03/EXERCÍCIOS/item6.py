#Escreva uma função que calcula o fatorial de um número inteiro fornecido pelo usuário.

import math

def fatorial(valor):
    valorFim = 1
    for i in range(valor, 0, -1):        
        valorFim = valorFim * i
    return valorFim

valor = int(input("Entre com o valor para calcularmos o fatorial dele: "))    
print(f"FATORIAL: {fatorial(valor)}")