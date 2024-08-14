def calcular_propriedades_retangulo(comprimento, largura):
    area = comprimento*largura
    perimetro = 2*(comprimento+largura)
    return area, perimetro

print(calcular_propriedades_retangulo(2, 3))