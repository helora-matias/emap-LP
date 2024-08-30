def termos(text, *args):
  linhas = text.splitlines()
  trans = transformation(linhas)
  for k in args:
    index = 1
    linhas = []
    for i in trans:
      for j in i:
          if j == k:
            if index in linhas:
              continue
            else:
              linhas.append(index)
      index += 1
    print(f'{k}: linhas {linhas}')

texto = """Este é o primeiro exemplo de linha.
Esta linha é a segunda linha do exemplo.
O terceiro exemplo está aqui.
Aqui temos a quarta linha de exemplo.
E finalmente, esta é a quinta linha de exemplo.
"""

print(termos(texto, 'linha', 'exemplo', 'segunda', 'quinta'))
