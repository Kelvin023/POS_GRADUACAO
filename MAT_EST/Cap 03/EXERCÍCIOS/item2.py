#Crie uma função que converte a temperatura de Celsius para Fahrenheit e vice-versa. O usuário deve informar a temperatura e a escala de origem.
import math

escalaOrigem = input("Informe a escala de origem: ")

if escalaOrigem != "C" and escalaOrigem != "c" and escalaOrigem != "F" and escalaOrigem != "f":
    print("\nINFORME UM VALOR VÁLIDO!")
    exit()

#Caso o usuario tenha informado um valor valido...    
valorEscalaOriginal = float(input("Entre com a temperatura a ser convertida: "))

if escalaOrigem == "F" or escalaOrigem == "f":
    valorEscalaFinal = (valorEscalaOriginal - 32) * 5/9
    print(f"Valor em Celsius: {valorEscalaFinal:.2f}")

elif escalaOrigem == "C" or escalaOrigem == "c":
    valorEscalaFinal = (valorEscalaOriginal * 9/5) + 32
    print(f"Valor em Fahrenheit: {valorEscalaFinal:.2f}")