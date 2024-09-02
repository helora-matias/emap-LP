import sys

i = 0
print(sys.getsizeof(1))
print(sys.getsizeof(1.0))
print(sys.getsizeof("A"))
print(sys.getsizeof(True))

n = int(sys.argv[1])

total = 0
for i in range(n+1):
    total += i

print(total)

j = 0
while j < n:
    print(j)
    j += 1

if n > 10:
    print("Verdadeiro")
elif n < 10:
    print("?")
else:
    print("Falso")
