"""
Escreva uma função que receba dois números naturais não-nulos m, n , que seguem duas restrições: m < n e m e n devem ser 
primos entre si. A função deve retornar uma matriz n × n preenchida com os números naturais de 1 a n^2 .

O preenchimento deve ser realizado no sentido horizontal, mas seguindo uma regra especial: a inserção dos números deve 
ser feita em passos de m em m casas. Caso m e n não atendam os requisitos, a função deve imprimir uma mensagem avisando 
do problema e retornar None.

Exemplo de retorno para m = 2 e n = 3 :

[[1 6 2],
 [7 3 8],
 [4 9 5]]

Exemplo de retorno para m = 3 e n = 5 :

[[1  18 10 2  19],
 [11 3  20 12 4 ],
 [21 13 5  22 14],
 [6  23 15 7  24],
 [16 8  25 17 9 ]]
"""

import numpy as np

def matriz(m, n):
    if m >= n:
        print("m deve ser menor do que n")
        return None

    for i in range(2, min(m,n) + 1):
      if m % i == 0 and n % i == 0:
        print("m e n devem ser primos entre si")
        return None 
    
    m_0 = np.zeros((n, n), dtype=int) #matriz de zeros
    matriz_in_list = list(range(1, n**2 + 1)) #lista com n**2 elementos
    e_alt = 0 #número que será alterado na lista

    for i in range(n):
      for j in range(n):
        m_0[i, j] =  matriz_in_list[e_alt]
        e_alt = (e_alt + m + n) % (n**2)

    return m_0

print(matriz(2, 3))
print(matriz(3, 5))
print(matriz(6, 10))