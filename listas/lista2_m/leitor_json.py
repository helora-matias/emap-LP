import modulo
import pprint
import json

def ex3():
    while True:
        try:
            file = input("Digite o nome do arquivo: ")
            conteudo = modulo.carrega_conteudos_json(file)
        except TypeError:
            print("O parâmetro `arquivo` não era uma string.")
        except FileNotFoundError:
            print("O arquivo não foi encontrado.")
        except IsADirectoryError:
            print("A string passada representa um diretório.")
        except PermissionError:
            print("Não há autorização para acessar o arquivo.")
        except OSError:
            print("Houve um problema do Sistema Operacional durante a leitura do arquivo.")
        except json.JSONDecodeError:
            print("Os conteúdos dentro do arquivo não estavam no formato de um `json`.")
        else:
            pprint.pprint(conteudo)

ex3()