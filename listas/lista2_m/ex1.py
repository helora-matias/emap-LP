"""
Implemente uma função em Python que receba como entrada um vetor (tupla de números) e calcule 
a norma Euclidiana desse vetor. A função deve realizar validações básicas de entrada para 
garantir que o vetor contém apenas números. Se a entrada for inválida, a função deve levantar 
uma exceção apropriada.
"""

def euclidiana(vetor):
    if not isinstance(vetor, tuple):
        raise TypeError("A entrada deve ser uma tupla.")
    somat = 0
    for i in range(len(vetor)):
        if not isinstance(vetor[i], (int, float)):
            raise ValueError("A entrada deve ser uma tupla de int ou float.")
        somat += (vetor[i])**2
    norma = somat**(1/2)
    return norma

v = ("1", 2)
print(euclidiana(v))

""" try:
    norm = euclidiana(v)
except TypeError:
    print("A entrada deve ser uma tupla.")
except ValueError:
    print("A entrada deve ser uma tupla de int ou float.")
else:
    print(norm)
 """