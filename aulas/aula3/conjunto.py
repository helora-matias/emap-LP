
""" Crie dois conjuntos com cores diferentes.
    Verifique se há alguma cor em comum entre os dois conjuntos.
    Adicione uma cor ao primeiro conjunto.
    Imprima a união dos dois conjuntos.
"""
# Vermelho, azul, amarelo, verde, laranja, rosa, roxo, marrom, preto, branco

cores1 = {"Amarelo", "Vermelho", "Marrom", "Verde", "Laranja"}
cores2 = {"Amarelo", "Roxo", "Marrom", "Rosa", "Azul"}

for i in cores2:
    for j in cores1:
        if i == j:
            print(i)
cores1.add("Preto")
print(cores1.union(cores2))
