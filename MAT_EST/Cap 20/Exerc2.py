"""O consumo de combustível (em km/l) de um determinado modelo de carro é normalmente distribuído com uma média de 12 km/l e um desvio padrão de 3 km/l.
Pergunta: Qual é a probabilidade de que um carro escolhido aleatoriamente tenha um consumo de combustível maior que 13 km/l?
"""

#START
from scipy.stats import norm

def calcProb(media, desvio_padrao, valor):
    # Calculando a probabilidade de que o consumo seja maior que o valor especificado
    probabilidade = 1 - norm.cdf(valor, loc=media, scale=desvio_padrao)  # CDF até o valor especificado
    return probabilidade

media = 12  # Média do consumo de combustível
desvio_padrao = 3  # Desvio padrão do consumo de combustível
valor = 13  # Valor de consumo de combustível a ser considerado

probabilidade = calcProb(media, desvio_padrao, valor)
print(f"\nA probabilidade de que um carro escolhido aleatoriamente tenha um consumo de combustível maior que {valor} km/l é: {probabilidade * 100:.1f}%")
#END