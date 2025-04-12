import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="Seno")
plt.plot(x, y2, label="Cosseno")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico de Seno e Cosseno")

#plt.legend()  # Adiciona a legenda automaticamente

plt.show()