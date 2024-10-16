"""
    Classe Base: Crie uma classe base chamada Personagem com atributos como nome, vida, 
    pontos_ataque e métodos como atacar() e info().

"""

class Personagem:
    def __init__(self, nome, vida, pontos_ataque):
        self.nome = nome
        self.vida = vida
        self.pontos_ataque = pontos_ataque

    def atacar(self, other):
        print(f'{self.nome} atacou {other.nome}.')
        print(f'Deixou {self.pontos_ataque} de dano.')
        other.vida -= self.pontos_ataque
    
    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Vida: {self.vida}')
        print(f'Ataque: {self.pontos_ataque}')

"""
Classes Derivadas: Desenvolva subclasses para diferentes tipos de personagens, 
como Heroi e Inimigo.
        Heroi pode ter atributos adicionais, como poder_especial.
        Inimigo pode incluir atributos como nivel_de_perigo.

    Métodos Específicos: Adicione métodos exclusivos, como usar_poder() para Heroi e fugir() 
    para Inimigo.
    Desafio: Implementar a lógica de combate entre um Heroi e um Inimigo, utilizando os 
    métodos de ataque e uma condição para verificar quem ganha.
"""

class Heroi(Personagem):
    def __init__(self, poder_especial):
        self.poder_especial = poder_especial

    def usar_poder(self, other):
        print(f'{self.nome} atacou {other.nome} com {self.poder_especial}')
        self.dano_poder = self.pontos_ataque
        other.vida -= self.pontos_ataque

class Inimigo(Personagem):
    def __init__(self, nivel_de_perigo):
        self.nivel_de_perigo = nivel_de_perigo
    
    def fugir(self):
        print(f'{self.nome} fugiu.')

def combate(heroi, inimigo):
    