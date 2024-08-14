def fibonacci(n, f1 = 0, f2 = 1):
    for i in range(n):
        print(f1)
        f1,f2 = f2,f1+f2

n = int(input("Digite um número: "))
fibonacci(n)