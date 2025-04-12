#Escreva um programa que calcula a média aritmética de uma lista de números fornecida pelo usuário.

import math

lista = []
numElementos = int(input("Entre com o número de elementos da lista: "))
soma = 0

print("##### AGORA PREENCHA CADA VALOR DA SUA LISTA ##### \n")
#Preechendo a lista
for i in range(numElementos):
    numero = int(input(f"Digite um número({i}): "))
    lista.append(numero)    
    soma = soma + numero
    
print(f"\nValor total da soma dos números informados: {soma}")
print(f"MÉDIA ARITMÉTICA DOS VALORES DA LISTA: {soma/numElementos}")