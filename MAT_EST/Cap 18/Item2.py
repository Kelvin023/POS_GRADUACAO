"""
Considere uma empresa que está lançando uma nova campanha de marketing por e-mail, destinada a promover um de seus produtos. 
A partir de experiências passadas, a empresa sabe que a taxa de abertura esperada para esses e-mails é de 20%. A campanha envolve o 
envio de 100 e-mails para potenciais clientes.

A empresa está interessada em saber qual é a probabilidade de pelo menos 25 desses e-mails serem abertos, o que considera um indicador 
de sucesso da campanha.
"""

#START
from scipy.stats import binom
# Definindo os parâmetros da distribuição binomial
n = 100  # Número de e-mails enviados
p = 0.20  # Probabilidade de um e-mail ser aberto
# Calculando a probabilidade de pelo menos 25 e-mails serem abertos
probabilidade = 1 - binom.cdf(24, n, p)  # CDF até 24 e-mails abertos
print(f"A probabilidade de pelo menos 25 e-mails serem abertos é: {probabilidade:.4f}")
#END