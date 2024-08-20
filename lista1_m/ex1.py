"""
Seja p o perimetro de um triângulo retângulo com lados {a, b, c} (a, b, c são números naturais). Se definimos p = 120, teremos três possíveis triângulos retângulos com perímetro p: 
{20, 48, 52}, {24, 45, 51}, {30, 40, 50}.

Escreva uma função que receba um inteiro n e retorne um inteiro representando qual valor de p ≤ n temos o maior número de triângulos possível. Se mais de um valor de p for adequado, 
a função deve retornar o menor deles.

Se a entrada da função não for um número inteiro, ela deverá imprimir uma mensagem avisando que só recebe inteiros e retornar None.
"""

def p_maior(n):
    if not isinstance(n, int):
        print("A função só recebe inteiros")
        return None
    triangulos = 0
    p_max = 0
    debug = 0
    for p in range(12, n+1):
        count = 0
        for a in range(1, p//2):
            for b in range(a, p//2):
                debug += 1
                c = p - a - b
                if (a**2 + b**2 == c**2):
                    count += 1
        if count > triangulos:
            triangulos = count
            p_max = p
    print(p_max)
    print(debug)

import time

itime = time.time()
p_maior(1000)
ftime = time.time()
print(ftime - itime)