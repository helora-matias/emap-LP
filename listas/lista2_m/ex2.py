"""
Dado dois pontos P_1 = ( x_1 , y_1 ) e P_2 = (x_2 , y_2) no plano cartesiano, implemente uma 
função em Python que calcule e retorne a equação da reta que passa por esses dois pontos na 
forma geral y = ax + b.
"""

def reta(p1, p2):
    if (not isinstance(p1, tuple)) or (not isinstance(p2, tuple)):
        raise TypeError("Os pontos devem ser tuplas.")
    if (len(p1) != 2) or (len(p2) != 2):
        raise ValueError("Os pontos devem ter tamanho 2")
    for i in range(2):
        if (not isinstance(p1[i], (int, float))) or (not isinstance(p2[i], (int, float))):
            raise ValueError("Os valores de x e y devem ser int ou float")
    if p1[0] == p2[0]:
        raise ZeroDivisionError("Os valores de x1 e x2 devem ser diferentes.")
    if (p1[0] == p2[0]) and (p[1] == p2[1]):
        raise ValueError("Os pontos devem ser diferentes.")
    a = (p1[1] - p2[1])/(p1[0] - p2[0])
    b = -a*p1[0] + p1[1]
    return a, b

p = (2, 0) 
q = (2, 6)

try:
    reta(p, q)
except TypeError:
    print("As entradas devem ser tuplas de tamanho 2.")
except ValueError:
    print("As entradas devem conter números (int ou float).")

else:
    print(reta(p, q))