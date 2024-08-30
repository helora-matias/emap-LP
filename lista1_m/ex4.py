"""
Agora generalize o problema, com uma função que receba um número qualquer de retângulos, por meio de argumentos nomeados 
(**kwargs), e retorne uma lista com tuplas. Cada tupla deve ter dois elementos, que equivalem a um par de retângulos que 
colidem (os nomes dos argumentos devem ser usados para representar um retângulo). A ordenação dos retângulos de uma tupla 
deve seguir a ordenação passada na função.

Se nenhum retângulo colidir, ou se nenhum ou apenas um retângulo for passado para a função, ela devera retornar uma lista 
vazia.
"""

def retangulos(**kwargs):

  for retangulo, vertices in kwargs.items():
    if len(vertices) != 4:
      print(f"O retângulo {retangulo} devem conter 4 vértices")
      return None

    for vertice in vertices:
      if len(vertice) != 2:
        print(f"Os vértices de {retangulo} devem ser representados como uma tupla de 2 elementos (x, y)")
        return None

    if vertices[0][0] != vertices[3][0] or vertices[1][0] != vertices[2][0] or vertices[0][1] != vertices[1][1] or vertices[2][1] != vertices[3][1]:
      print(f"O retângulo {retangulo} precisa estar paralelo aos eixos e a ordem dos pontos deve iniciar no lado superior esquerdo e seguir no sentido horário")
      return None

  colisoes = []
  rets = list(kwargs.keys())

  for i in range(len(rets)):
    ret1 = kwargs[rets[i]]
    for j in range(i + 1, len(rets)):
      ret2 = kwargs[rets[j]]
      for vertice in ret2:
        if ret1[0][0] <= vertice[0] <= ret1[1][0] and ret1[3][1] <= vertice[1] <= ret1[0][1]:
          colisoes.append((rets[i], rets[j]))

  return colisoes

a = ((3, 4), (7, 4), (7, 2), (3, 2))
b = ((0, 3), (4, 3), (4, 0), (0, 0))
c = ((1, 4), (4, 4), (4, 1), (1, 1))
d = ((2, 2), (2, 5), (5, 5), (5, 2))
e = ((6, 8), (8, 8), (8, 6), (6, 6))
f = ((0, 0), (3, 0), (3, 3), (0, 3))
h = ((0, 0), (3, 1), (3, 4), (0, 3))

print(retangulos(a=a, d=d))
print(retangulos(a=a, h=h))
print(retangulos(a=a, b=b, c=c, e=e, f=f))
