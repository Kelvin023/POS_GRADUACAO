#Crie um gráfico da função y = sin(x) para valores de x no intervalo de 0 a 2π.
import math as mt
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)


# Criando uma massa de dados no intervalo de 0 a 2π, contendo 100 valores
x = np.linspace(0, 2*(mt.pi), 100)
#print(x)

y = f(x)

# Cria o gráfico
plt.figure(figsize = (6, 4))
plt.plot(x, y, label = 'y = sin(x)')

# Adiciona um título e rótulos aos eixos
plt.title('FUNÇÃO SENO')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma legenda
plt.legend()

# Mostra o gráfico
plt.grid(True)
plt.show()