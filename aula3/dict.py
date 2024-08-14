
""" Crie um dicionário com informações sobre um livro (título, autor, ano de publicação).
    Imprima o título do livro.
    Atualize o ano de publicação do livro.
    Remova o autor do dicionário.
"""

dict = {"titulo": "O Código Da Vinci", "autor": "Dan Brown", "ano": 2000}
print(dict.get("titulo"))
dict.update({"ano": 2003})
print(dict)
dict.pop("autor")
print(dict)