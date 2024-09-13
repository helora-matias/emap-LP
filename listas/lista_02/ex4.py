




"""
Escreva uma função para calcular a média móvel dos preços de ações em uma janela de 5 dias. 
Gere um array NumPy de 30 preços de ações aleatórios (números de ponto flutuante) e retorne o 
array das médias móveis.
"""
import numpy as np

def media_movel(precos):
    medias = []
    for i in range(len(precos)-4):
        m = np.mean(precos[i:i+5])
        medias.append(m)
        print(medias)

precos = np.array([10.0, 12.5, 13.0, 14.5, 15.0, 14.0, 13.5])
media_movel(precos)

""" 
precos = np.random.random(30)
print(precos)
"""
"""
# Entrada
precos = np.array([10.0, 12.5, 13.0, 14.5, 15.0, 14.0, 13.5])
# Saida
medias_moveis = [13.16, 13.75, 14.0]
"""