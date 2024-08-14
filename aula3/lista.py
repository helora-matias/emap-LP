
""" Crie uma lista com os nomes de cinco pessoas.
    Adicione o seu próprio nome à lista.
    Remova o nome da segundo pessoa da lista.
    Imprima a lista de amigos em ordem alfabética.
"""

list = ["Victor", "Gabriel", "Haruo", "Iwamoto", "Timóteo"]
list.append("Helora")
list.pop(1)
list.sort()
print(list)