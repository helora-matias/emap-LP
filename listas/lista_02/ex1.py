




"""
Gere um array de 20 números inteiros aleatórios entre 1 e 100. Escreva uma função para 
separar os números pares dos números ímpares, retornando dois novos arrays.
"""

import numpy as np

def pares_impares(numeros):
    pares = numeros[numeros % 2 == 0]
    impares = numeros[numeros % 2 != 0]
    return pares, impares

numeros = np.random.randint(1, 101, 20)
print(f'Array = {numeros}')

separation = pares_impares(numeros)
print(f'Pares: {separation[0]}')
print(f'Ímpares: {separation[1]}')

"""
# Entrada
numeros = np.array([15, 26, 33, 42, 55, 68, 71, 88, 90, 91])

# Saida
pares = [26, 42, 68, 88, 90]
ímpares = [15, 33, 55, 71, 91]
"""
