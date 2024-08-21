"""
Escreva uma função que receba dois números naturais m , n , que seguem duas restrições: m < n 
e m não pode ser divisor de n (com excessão do caso m = 1 que pode ser permitido). A função 
deve retornar uma matriz n × n preenchida com os números naturais de 1 a n 2 .

O preenchimento deve ser realizado no sentido horizontal, mas seguindo uma regra especial: a 
inserção dos números deve ser feita em passos de m em m casas. Caso m e n não atendam os 
requisitos, a função deve imprimir uma mensagem avisando do problema e retornar None.

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
    if m != 1 and n % m == 0:
        print("m não pode ser divisor de n")
        return None
    
    m_0 = np.zeros((n, n))
    e_alterados = 0
    #while e_alterados < n**2:
        #for i in range(n**2):

    #for i in np.nditer(m_0):
        #print(i)

""" m_0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
for i in np.nditer(m_0):
    print(i)
for j in np.ndenumerate(m_0):
    print(f'j = {j}')
for k in np.ndindex(m_0.shape):
    m_0[k] = 10    
    
print(m_0)

""" 
m_0 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
e = np.reshape(m_0, (1, 1))
print(e)
"""
3 x 3
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
"""