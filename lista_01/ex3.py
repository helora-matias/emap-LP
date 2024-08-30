def matriz_por_matriz(matriz1, matriz2):
  vetor = []
  for i in range(len(matriz1)):
    vetor2 = []
    for j in range(len(matriz2[0])):
      soma = 0
      for k in range(len(matriz1[0])):
        produto = matriz1[i][k]*matriz2[k][j]
        soma += produto
        #print(produto)
      vetor2.append(soma)
    vetor.append(vetor2)
  print(vetor)
 
matriz1 = [
    [1, 2],
    [3, 4]
]
matriz2 = [
    [5, 6],
    [7, 8]
]
resultado = matriz_por_matriz(matriz1, matriz2)
# resultado deve ser [[19, 22], [43, 50]]
