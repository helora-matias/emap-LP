




"""
Normalize um array 1D de notas de exames (números inteiros aleatórios entre 0 e 100) para uma 
escala de 0 a 1 usando a fórmula:

normalized = (x − min ( x )) / (max ( x ) − min ( x )) 
"""
import numpy as np

def normalizacao(notas):
    normalized = (notas - np.min(notas))/(np.max(notas) - np.min(notas))
    return normalized

array = np.random.randint(1, 101, 5)

print(f'Array = {array}')
print(f'Notas normalizadas = {normalizacao(array)}')