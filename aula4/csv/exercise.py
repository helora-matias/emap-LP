"""
    Escreva um programa que leia um arquivo CSV chamado "dados.csv" e calcule a média de uma 
    coluna numérica específica.
    Escreva uma função que receba uma lista de dicionários representando dados tabulares e 
    salve esses dados em um arquivo CSV chamado "saida.csv".
"""

import csv

notas = [
    ["Aluno", "Nota"],
    ["João", 5.0],
    ["Paula", 8.0],
    ["Vitória", 10.0],
]

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in notas:
        escritor_csv.writerow(linha)

with open('dados.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        for coluna in linha:
            print(coluna)

