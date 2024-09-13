



"""
Você tem as coordenadas de cinco cidades em um plano 2D, representadas por seus valores de 
latitude e longitude. Escreva uma função que calcule a distância de Manhattan entre cada par 
de cidades.

d Manhattan = | x 2 − x 1 | + | y 2 − y 1 | 
"""
import numpy as np

def dist_manhattan(cidades):
    dists = np.array()
    for i in range(5):
        for j in range(5):
            x = cidades[i][0] - cidades[j][0]
            y = cidades[i][1] - cidades[j][1]
            dist = np.abs(x) + np.abs(y)
            np.append(dists, dist)
            print(dists)

cidades = np.array([[50, -120], [40, -70]])

print(cidades[0])
print(cidades[1])

x = cidades[0][0] - cidades[1][0]
y = cidades[0][1] - cidades[1][1]
print(x)
print(y)
dist = np.abs(x) + np.abs(y)
print(dist)

dist_manhattan(cidades)

"""
# Entrada
cidades = np.array([[50, -120], 
                    [40,  -70]])
# Saida
distância_manhattan = 60
"""