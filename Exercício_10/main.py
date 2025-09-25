import sys

def potencia(base, exp):
    # caso base: qualquer número elevado a 0 é 1
    if exp == 0:
        return 1
    # passo recursivo: base^exp = base * base^(exp-1)
    return base * potencia(base, exp - 1)

# lê a entrada
entrada = sys.stdin.read().strip().split()
base = int(entrada[0])
exp = int(entrada[1])

# calcula e imprime
resultado = potencia(base, exp)
print(resultado)
