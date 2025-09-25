import sys

def mdc(a, b):
    # Caso base: se o segundo número for 0, o MDC é o primeiro
    if b == 0:
        return a
    # Passo recursivo: mdc(a, b) = mdc(b, a % b)
    return mdc(b, a % b)

# lê a entrada
entrada = sys.stdin.read().strip().split()
a = int(entrada[0])
b = int(entrada[1])

# calcula e imprime o resultado
print(mdc(a, b))
