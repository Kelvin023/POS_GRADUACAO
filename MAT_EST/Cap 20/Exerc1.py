"""
Suponha que o tempo de produção de um carro em uma fábrica siga uma distribuição normal com uma média de 20 horas e 
um desvio padrão de 2 horas. Pergunta: Qual é a probabilidade de que um carro seja produzido em menos de 18 horas?
"""

#START
from scipy.stats import norm
# Definindo os parâmetros da distribuição normal
media = 20  # Média do tempo de produção
desvio_padrao = 2  # Desvio padrão do tempo de produção

# Calculando a probabilidade de que um carro seja produzido em menos de 18 horas
probabilidade = norm.cdf(18, loc=media, scale=desvio_padrao)    # CDF até 18 horas
print(f"A probabilidade de que um carro seja produzido em menos de 18 horas é: {probabilidade * 100:.1f}%")
#END