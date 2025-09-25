import sys

def fatorial(n):
    # caso base: fatorial de 0 e 1 é 1
    if n == 0 or n == 1:
        return 1
    # passo recursivo: n! = n * (n-1)!
    return n * fatorial(n - 1)

# lê a entrada
entrada = sys.stdin.read().strip()
n = int(entrada)

# calcula e imprime o resultado
print(fatorial(n))
