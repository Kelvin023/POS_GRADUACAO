#Crie um programa que gera a sequência de Fibonacci até um determinado número n fornecido pelo usuário.

import math

def seqFibonacci(qtdTermos):
    lista = [1,1]
    i = 2
    while (i < qtdTermos):
        lista.append(lista[i-1] + lista[i-2])
        i = i + 1
    print(lista)


#START
qtdTermos= int(input("Entre com o número de termos da sequencia de Fibonacci: "))
seqFibonacci(qtdTermos)