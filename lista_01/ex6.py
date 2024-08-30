def obter_estatisticas(text):
  linhas = text.splitlines()
  trans = transformation(linhas)
  print(trans)
  qtd_tot = 0
  for i in trans:
    qtd_i = len(i)
    qtd_tot += qtd_i
  print(f"Número total de palavras: {qtd_tot}")

  dict = {}
  for i in trans:
    qtd = 0
    for j in i:
      if j in dict:
        continue
      else:
        qtd += 1
        dict[j] = qtd
        print(dict)


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
