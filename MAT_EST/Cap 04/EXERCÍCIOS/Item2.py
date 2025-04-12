#Desenhe o gráfico da função y = x^2 - 4x + 4. Crie uma massa de dados de exemplo usando np.linspace().
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 - 4*x + 4


# Criando uma massa de dados por meio de um conjunto de valores (por exemplo, de -10 a 20). Vamos usar 100 valores
x = np.linspace(-2, 6, 100)
#print(x)

y = f(x)

# Cria o gráfico
#plt.figure(figsize = (6, 4))
plt.plot(x, y, label = 'y = x^2 - 4x + 4')

# Adiciona um título e rótulos aos eixos
plt.title('FUNÇÃO QUADRÁTICA')
plt.xlabel('x')
plt.ylabel('y')

# Adiciona uma legenda
plt.legend()

# Mostra o gráfico
plt.grid(True)
plt.show()