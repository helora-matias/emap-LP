"""
Construa uma função que receba dois retângulos e retorne um booleano indicando se eles colidem. Um retângulo é 
representado como uma tupla de 4 elementos, cada um sendo um dos vértices do retângulo, iniciando do superior esquerdo 
e avançando em sentido horário. Cada vértice é representado como uma tupla, contendo coordenadas x e y do plano cartesiano.

Considere que os retângulos não são rotacionados (isto é, as arestas são paralelas aos eixos) e que dois retângulos 
colidem se um dos vértices de um deles está contido no conjunto fechado delimitado pelo outro retângulo.

Se um dos retẫngulos estiver representado incorretamente, a função deverá retornar None e mostrar uma mensagem indicando 
o problema com o input.
"""

def retangulos(a, b):
  if len(a) != 4 or len(b) != 4:
    print("Os retângulos devem conter 4 vértices")
    return None

  for vertice in a:
    if len(vertice) != 2:
      print("Os vértices devem ser representados como uma tupla de 2 elementos (x, y)")
      return None

  for vertice in b:
    if len(vertice) != 2:
      print("Os vértices devem ser representados como uma tupla de 2 elementos (x, y)")
      return None

  if a[0][0] != a[3][0] or a[1][0] != a[2][0] or a[0][1] != a[1][1] or a[2][1] != a[3][1]:
    print(f"O retângulo {a} precisa estar paralelo aos eixos e a ordem dos pontos deve iniciar no lado superior esquerdo e seguir no sentido horário")
    return None
  if b[0][0] != b[3][0] or b[1][0] != b[2][0] or b[0][1] != b[1][1] or b[2][1] != b[3][1]:
    print(f"O retângulo {b} precisa estar paralelo aos eixos e a ordem dos pontos deve iniciar no lado superior esquerdo e seguir no sentido horário")
    return None

  for vertice in b:
    if a[0][0] <= vertice[0] <= a[1][0] and a[3][1] <= vertice[1] <= a[0][1]:
      return True
    
  return False

a = ((3, 4), (7, 4), (7, 2), (3, 2))
b = ((0, 3), (4, 3), (4, 0), (0, 0))
c = ((0, 0), (3, 1), (3, 4), (0, 3))
d = ((2, 2), (2, 5), (5, 5), (5, 2))

retangulos(a, c)
retangulos(b, d)
retangulos(b, a)