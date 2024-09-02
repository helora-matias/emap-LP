def distancia_euclidiana(v1, v2):
    quad = 0
    for i in range(len(v1)):
        sub = v1[i] - v2[i]
        quad += sub**2
    dist = quad**(1/2)
    return dist

v1 = (2,2)
v2 = (1,1)

try:
    distancia_euclidiana(v1, v2)
except TypeError:
    print("Erro: As variáveis devem ser listas de floats ou inteiros.")
except IndexError:
    print("Erro: Os vetores devem ter o mesmo tamanho.")
else:
    print(distancia_euclidiana(v1, v2))
