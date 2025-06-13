"""
Suponha que as notas de uma prova em uma turma sigam uma distribuição normal com uma média de 70 e um desvio padrão de 12. 
Pergunta: Qual é a probabilidade de que um aluno escolhido aleatoriamente tenha uma nota maior que 80?
"""

from scipy.stats import norm

def calcProb(media, desvio_padrao, valor):
    # Calculando a probabilidade de que a nota seja MAIOR que o valor especificado
    probabilidade = 1 - norm.cdf(valor, loc=media, scale=desvio_padrao)  # CDF até o valor especificado
    return probabilidade

#START
media = 70  # Média das notas
desvio_padrao = 12  # Desvio padrão das notas	
valor = 80  # Valor da nota a ser considerado

probabilidade = calcProb(media, desvio_padrao, valor)
print(f"\nA probabilidade de que um aluno escolhido aleatoriamente tenha uma nota maior que {valor} é: {probabilidade * 100:.1f}%")
#END