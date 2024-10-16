class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def info(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano de Publicação: {self.ano_publicacao}')

class LivroFisico(Livro):
    def __init__(self, peso):
        self.peso = peso

    def informar_localizacao(self):

class Ebook(Livro):
    def __init__(self, formato, tamanho):
        self.formato = formato
        self.tamanho = tamanho

    def download(self):


