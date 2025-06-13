"""
As notas finais de uma turma em uma disciplina específica são normalmente distribuídas com uma média de 60 e um desvio padrão de 15. 
Pergunta: Qual é a probabilidade de que um aluno escolhido aleatoriamente tenha uma nota final entre 50 e 70?
"""

from scipy.stats import norm

#START
media = 60  # Média das notas finais
desvio_padrao = 15  # Desvio padrão das notas finais

ProbAcima = norm.cdf(70, loc=media, scale=desvio_padrao)  # CDF até 70
ProbAbaixo = norm.cdf(50, loc=media, scale=desvio_padrao)  # CDF até 50
probabilidade = ProbAcima - ProbAbaixo
print(f"A probabilidade de que um aluno escolhido aleatoriamente tenha uma nota final entre 50 e 70 é: {probabilidade * 100:.1f}%")
#END