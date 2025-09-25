import sys

def serie_harmonica(n):
    # caso base
    if n == 1:
        return 1
    # passo recursivo
    return 1/n + serie_harmonica(n-1)

# lê a entrada
entrada = sys.stdin.read().strip()
n = int(entrada)

# calcula a série
resultado = serie_harmonica(n)

# imprime com 3 casas decimais
print(f"{resultado:.3f}")
