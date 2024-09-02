A = "O gato está no telhado."
B = "O gato dorme no telhado."

texts = []
texts.append(A)
texts.append(B)

def transformation(list):
  palavras = []
  for i in list:
    t = i.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    mini = t.lower()
    palavras_i = mini.split()
    palavras.append(palavras_i)
  return palavras

palavras = transformation(texts)
print(palavras)

intersection = []
for i in palavras[0]:
  for j in palavras[1]:
    if i == j:
      intersection.append(i)
print(intersection)

union = []
for i in palavras:
  for j in i:
    if j in union:
      continue
    else:
      union.append(j)
print(union)

jaccard = len(intersection)/len(union)
print(jaccard)
