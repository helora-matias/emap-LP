def calcular_media(**kwargs):
    for nome in kwargs:
        media = kwargs[nome]
        print(f'O aluno {nome} teve média final {media}')

calcular_media(Joao= 2.5, Pedro= 8.0)