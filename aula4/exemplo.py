import csv

with open('dados.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        print(linha)

dados = [
    ['Nome', 'Idade'],
    ['Alice', 30],
    ['Bob', 35],
    ['Charlie', 25]
]

with open('saida.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    for linha in dados:
        escritor_csv.writerow(linha)