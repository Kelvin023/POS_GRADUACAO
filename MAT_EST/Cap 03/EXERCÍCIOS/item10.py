#Crie uma função que verifica se um número fornecido pelo usuário é primo ou não.

import math

def primo(num):
    lista = []
    soma = 0
    for i in range(num, 0, -1):        
        if (num%i)==0:
            soma = soma + 1
            lista.append(i)
    if soma == 2:
        print("### NÚMERO INFORMADO É PRIMO! ###")
        print("SEGUE OS DIVISORES DO NÚMERO INFORMADO: ", lista)
    else:
        print(f"### NÚMERO INFORMADO NÃO É PRIMO! ESSE CARA TEM {soma} DIVISORES ###")
        print("SEGUE OS DIVISORES DO NÚMERO INFORMADO: ", lista)

#START
numero = int(input("Entre com um número para informarmos se ele é primo ou não: "))
primo(numero)