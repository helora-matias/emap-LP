



"""
Crie uma função que realiza um sumário estatístico básico de um array NumPy. Ela deve calcular 
e exibir o valor mínimo, o valor máximo e os quartis (25%, 50%, e 75%) de um array fornecido.
"""
import numpy as np

def sumario(array):
    min = np.min(array)
    max = np.max(array)
    q1 = np.percentile(array, 25)
    q2 = np.percentile(array, 50)
    q3 = np.percentile(array, 75)
    return min, max, q1, q2, q3

array = np.array([10, 20, 35, 50, 70, 80, 95, 100])

s1 = sumario(array)

print("Sumário Estatístico do Array:")
print(f"Valor Mínimo: {s1[0]}")
print(f"Valor Máximo: {s1[1]}")
print(f"Quartis:")
print(f"  25%: {s1[2]}")
print(f"  50% (Mediana): {s1[3]}")
print(f"  75%: {s1[4]}")

"""
# Entrada
array = np.array([10, 20, 35, 50, 70, 80, 95, 100])
# Saída:
# Sumário Estatístico do Array:
# Valor Mínimo: 10
# Valor Máximo: 100
# Quartis:
#   25%: 31.25
#   50% (Mediana): 60.0
#   75%: 83.75
"""