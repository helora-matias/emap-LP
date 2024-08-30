def transformation(list):
  palavras = []
  for i in list:
    t = i.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    mini = t.lower()
    palavras_i = mini.split()
    palavras.append(palavras_i)
  return palavras

def obter_estatisticas(text):
  linhas = text.splitlines()
  trans = transformation(linhas)
  qtd_tot = 0
  for i in trans:
    qtd_i = len(i)
    qtd_tot += qtd_i
  print(f"Número total de palavras: {qtd_tot}")

  dictionary = {}
  for i in trans:
    for j in i:
      if j in dictionary:
        dictionary[j] += 1
      else:
        dictionary[j] = 1

  def my_func(e):
      return e[1]
  ordenados = list(sorted(dictionary.items(), key=my_func, reverse=True))

  print("")
  print("Top 5 palavras mais frequentes:")
  index = 0
  for i in ordenados:
    while index < 5:
      print(f"{index+1}. {ordenados[index][0]}: {ordenados[index][1]}")
      index += 1

  new_dict = {}
  for i in range(len(trans[0])-1):
    two = trans[0][i] + ' ' + trans[0][i+1]
    if two in new_dict:
      new_dict[two] += 1
    else:
      new_dict[two] = 1

  ordenados1 = list(sorted(new_dict.items(), key=my_func, reverse=True))

  print("")
  print("Top 5 palavras mais frequentes:")
  index = 0
  for i in ordenados1:
    while index < 5:
      print(f"{index+1}. {ordenados1[index][0]}: {ordenados1[index][1]}")
      index += 1
    

texto = "A programação em Python é divertida. A programação é poderosa e simples. Python é uma linguagem versátil."
obter_estatisticas(texto)

# Número total de palavras: 15

# Top 5 palavras mais frequentes:
# 1. é: 3
# 2. a: 2
# 3. programação: 2
# 4. python: 2
# 5. em: 1

# Top 5 sequências de duas palavras mais frequentes:
# 1. a programação: 2
# 2. python é: 2
# 3. programação em: 1
# 4. em python: 1
# 5. é divertida: 1
