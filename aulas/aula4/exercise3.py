""" 
    Escreva um programa que leia um arquivo JSON chamado "dados.json" e exiba na tela o valor de uma chave específica.
    Escreva uma função que receba um dicionário e salve esse dicionário em um arquivo JSON chamado "saida.json".
"""

import json

dados = {'nomes': 'Alice', 'idades': 30, 'cidades': 'São Paulo'}


dados = {
    'nomes': {'Alice': 'Maria'}, 
    'idades': ['30', '45', '20'],
    'cidades': ['São Paulo', 'Rio de Janeiro', 'Maceió'],
    'random' : 2
}


with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json)

with open('dados.json', 'r') as arquivo_json:
    dados_json = json.load(arquivo_json)
    print(dados_json.keys())
    print(list(dados_json.keys())[1])

# def function(dict):
#     with open('saida.json', 'w') as arquivo_json:
#         json.dump(dict, arquivo_json)

# dict = {
#     "usuário": {
#         "nome" : "Helora",
#         "idade" : 18
#     },
#     "acesso": {
#         "login" : "B435990",
#         "senha": "123456"
#     }
# }

# function(dict)