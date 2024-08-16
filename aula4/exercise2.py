"""
    Escreva um programa que leia um arquivo CSV chamado "dados.csv" e calcule a média de uma coluna numérica específica.
    Escreva uma função que receba uma lista de dicionários representando dados tabulares e salve esses dados em um arquivo CSV chamado "saida.csv".
"""

import csv

notas = [
    ["João", 5.0],
    ["Paula", 8.0],
    ["Vitória", 10.0],
]

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in notas:
        escritor_csv.writerow(linha)

soma = 0
i = 0

with open('dados.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        soma += float(linha[1]) 
        i += 1

average = soma/i
print(average)

def function(list_dict):
    with open('saida.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerows(list_dict, ',')

    with open('saida.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            print(linha)

list_dict = [
    {'nomes': ['Amanda', 'Bia', 'Josefa']},
    {'idades': [20, 30, 40]},
    {'cidades': ['Manaus', 'Espírito Santo', 'Belo Horizonte']}
]

function(list_dict)
