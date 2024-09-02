""" 
Crie um módulo chamado operacoes_matematicas.py que contenha as seguintes funções:
- adicionar(a, b): Retorna a soma de a e b.
- subtrair(a, b): Retorna a subtração de b de a.
- multiplicar(a, b): Retorna a multiplicação de a por b.
- dividir(a, b): Retorna a divisão de a por b, tratando a divisão por zero.

Crie um script separado main.py que importe o módulo operacoes_matematicas e teste todas as 
funções com diferentes valores.
"""

def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("Não é possível dividir qualquer número por 0.")
    else:
        return a / b