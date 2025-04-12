#Crie um gráfico para a função y = e^x para valores de x no intervalo de -2 a 2.
import math as mt
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return (np.e)**x


# Criando uma massa de dados no intervalo de -2 a 2
x = np.linspace(-2, 2)
y = f(x)

# Cria o gráfico
#plt.figure(figsize = (6, 4))
plt.plot(x, y, label = 'y = e^x')

# Adiciona um título e rótulos aos eixos
plt.title('NÚMERO DE EULER ELEVADO A X')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma legenda
#plt.legend()

# Mostra o gráfico
plt.grid(True)
plt.show()