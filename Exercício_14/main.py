import sys

def fibonacci(n):
    # casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # passo recursivo
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# lê a entrada
entrada = sys.stdin.read().strip()
n = int(entrada)

# calcula e imprime o resultado
print(fibonacci(n))
