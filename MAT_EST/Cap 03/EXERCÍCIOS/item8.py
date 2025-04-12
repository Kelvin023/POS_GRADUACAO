#Faça um programa que calcula o montante final de um investimento com juros compostos. 
# O usuário deve fornecer o capital inicial, a taxa de juros anual, e o número de anos

#Montante Final = Valor Inicial * (1 + Taxa de Juros)^Tempo de Aplicação

import math

def calcMontanteFinal (valCapInicial, rtAnual, qtdAnos):
    return valCapInicial * ((1 + rtAnual)**qtdAnos)

valCapitalInicial = float(input("Informe o valor de capital inicial: "))
rtAnual = float(input("Informe o valor da taxa de juros anual: "))
qtdAnos = int(input("Informe o número de anos: "))

print(f"\nLEVANDO EM CONTA OS VALORES INFORMADOS, O MONTANTE FINAL É DE: R${calcMontanteFinal(valCapitalInicial, rtAnual, qtdAnos):.2f}")