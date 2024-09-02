def matriz_por_vetor(matriz, vetor):
  matriz_resultado = []
  for i in matriz:
    produto = sum(a * b for a, b in zip(i, vetor))
    matriz_resultado.append(produto)
  print(matriz_resultado)

matriz = [
    [1, 2],
    [3, 4],
    [5, 6]
]
vetor = [7, 8]
resultado = matriz_por_vetor(matriz, vetor)
