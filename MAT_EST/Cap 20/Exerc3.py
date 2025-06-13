"""
O peso dos automóveis produzidos por uma fábrica segue uma distribuição normal com uma média de 1500 kg e um desvio padrão de 50 kg. 
Pergunta: Qual é a probabilidade de que um automóvel produzido tenha um peso entre 1450 kg e 1550 kg?
"""

from scipy.stats import norm

#START
media = 1500  # Média do peso dos automóveis
desvio_padrao = 50  # Desvio padrão do peso dos automóveis

ProbAcima = norm.cdf(1550, loc=media, scale=desvio_padrao)  # CDF até 1550 kg
ProbAbaixo = norm.cdf(1450, loc=media, scale=desvio_padrao)  # CDF até 1450 kg

probabilidade = ProbAcima - ProbAbaixo
print(f"A probabilidade de que um automóvel produzido tenha um peso entre 1450 kg e 1550 kg é: {probabilidade * 100:.1f}%")
#END