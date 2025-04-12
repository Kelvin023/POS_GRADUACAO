#Crie um gráfico para a função y = 2x + 3 para valores de x no intervalo de 5 a 10.
import numpy as np
import matplotlib.pyplot as plt

# Cria um conjunto de valores de x (por exemplo, de 5 a 10)
x = np.linspace(5, 10, 30)

def f(x):
    return 2*x + 3

y = f(x)

# Cria o gráfico
plt.figure(figsize = (6, 4))
plt.plot(x, y, label = 'y = 2x + 3')

# Adiciona um título e rótulos aos eixos
plt.title('Dobro de x  + 3')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma legenda
plt.legend()

# Mostra o gráfico
plt.grid(True)
plt.show()