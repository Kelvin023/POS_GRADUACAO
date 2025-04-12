#Desenhe o gráfico de y = log(x) (logaritmo natural) para valores de x no intervalo de 0.1 a 10.

import math as mt
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log(x)


# Criando uma massa de dados no intervalo de 0.1 a 10
x = np.linspace(0.1, 10)
y = f(x)

# Cria o gráfico
plt.figure(figsize = (6, 4))
plt.plot(x, y, label = 'y = log(x)')

# Adiciona um título e rótulos aos eixos
plt.title('LOGARITMO NATURAL')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma legenda
plt.legend()

# Mostra o gráfico
plt.grid(True)
plt.show()