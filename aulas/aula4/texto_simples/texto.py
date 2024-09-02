"""
    Escreva um programa que abra um arquivo de texto chamado "texto.txt", 
    leia o conteúdo e exiba na tela.
    Escreva uma função que receba uma lista de strings e salve essas strings em um arquivo 
    de texto chamado "saida.txt", cada string em uma linha separada.
"""

print("Tarefa 1")
arquivo = open("texto.txt", "r", encoding = "utf-8")
conteudo = arquivo.read()
print(conteudo)

def list_string(list):
    file = open("saida.txt", "x", encoding = "utf-8")
    for string in list:
        file.write(f'{string}\n')
    file = open("saida.txt", "r")
    ct = file.read()
    print(ct)

print("\nTarefa 2")
list = ["oi", "tudo", "bem", "?"]
list_string(list)