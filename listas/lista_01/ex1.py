def produto_interno(vetor1, vetor2):
  soma = 0
  for i in vetor1:
    soma += i*vetor2[vetor1.index(i)]
  return soma

vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
print(produto_interno(vetor1, vetor2))
