import numpy as np
import matplotlib.pyplot as plt

# Gerando dados de exemplo: preços de casas
np.random.seed(0)
precos_casas = np.random.lognormal(mean = 13, sigma = 0.6, size = 1000)

# Aplicando a transformação logarítmica
precos_casas_log = np.log(precos_casas)

# Criando os gráficos para comparação
plt.figure(figsize = (8, 4))

# Gráfico dos dados originais
plt.subplot(1, 2, 1)
plt.hist(precos_casas, bins = 30, color = 'blue', alpha = 0.7)
plt.title('Distribuição dos Preços das Casas')
plt.xlabel('Preço')
plt.ylabel('Frequência')

# Gráfico dos dados transformados
plt.subplot(1, 2, 2)
plt.hist(precos_casas_log, bins = 30, color = 'green', alpha = 0.7)
plt.title('Distribuição Logarítmica dos Preços das Casas')
plt.xlabel('Log do Preço')
plt.ylabel('Frequência')

plt.tight_layout()
plt.show()