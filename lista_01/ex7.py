"""
Um CPF (Cadastro de Pessoas Físicas) é composto por 11 dígitos numéricos, geralmente apresentados
no formato "XXX.XXX.XXX-YY". Para ser considerado válido, um CPF deve atender aos seguintes 
critérios:
    1. Deve conter 11 dígitos numéricos.
    2. Não deve consistir de todos os dígitos iguais (por exemplo, "111.111.111-11" não é um 
    CPF válido).
    3. Deve obedecer ao algoritmo de validação do CPF, descrito a seguir:
        Os primeiros 9 dígitos são os números base.
        O 10º dígito (primeiro dígito verificador) é calculado da seguinte forma:
            Multiplique os 9 primeiros dígitos pela sequência decrescente de 10 a 2.
            Some os resultados dessas multiplicações.
            Calcule o resto da divisão dessa soma por 11.
            Se o resto for menor que 2, o dígito verificador é 0. Se for maior ou igual a 2, o 
            dígito verificador é 11 menos o resto.
        O 11º dígito (segundo dígito verificador) é calculado da mesma forma, mas agora com a 
        sequência decrescente de 11 a 2 (considerando os 9 dígitos base mais o primeiro dígito 
        verificador).

Implemente a função valida_cpf(cpf) que recebe uma string representando o CPF no formato "XXX.XXX.XXX-YY" e retorna um valor booleano indicando se o CPF é válido ou não.
"""

def valida_cpf(cpf):
    t = cpf.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
    if len(t) != 11:
        return False
    todos = 1
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            todos+=1
    if todos == 11:
        return False
    print(t)

valida_cpf("111.111.111-11")