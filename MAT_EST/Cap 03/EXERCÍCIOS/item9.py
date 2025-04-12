#Escreva um programa que converte uma quantidade de uma moeda (como dólar) para outra (como euro), considerando uma taxa de câmbio fornecida pelo usuário.

import math

def conversao(valorMoeda, rtCambio):
    return valorMoeda * rtCambio

valDolar = float(input("Informe a quantia em dólares a ser convertida para euros: "))
rtCambio = float(input("Informe a taxa de câmbio: "))

print(f"O valor de {valDolar} convertido em euro e de acordo com a taxa de cambio {rtCambio} vai ser de: {conversao(valDolar, rtCambio)}")