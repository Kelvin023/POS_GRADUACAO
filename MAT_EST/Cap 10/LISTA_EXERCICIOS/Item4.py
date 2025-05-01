#Utilize a biblioteca Numpy para calcular a inversa de uma matriz 3x3. Considere esta matriz abaixo para o cálculo. Use try/except para tratar eventuais erros.

import numpy as np

#START
matriz = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]

try:
    inversa = np.linalg.inv(matriz)
    print(f"Inversa da matriz {matriz} é: {inversa}")
except np.linalg.LinAlgError as e:
    print(f"Erro: {e}. A matriz não é inversível.") 
#END