import sys

def conta_maiusculas_minusculas(texto):
    maiusculas = 0
    minusculas = 0
    for c in texto:
        if c.isupper():
            maiusculas += 1
        elif c.islower():
            minusculas += 1
    return maiusculas, minusculas

# lê a entrada
entrada = sys.stdin.read().strip()

# chama a função
maiusc, minusc = conta_maiusculas_minusculas(entrada)

# imprime resultado
print(f"Maiúsculas: {maiusc}")
print(f"Minúsculas: {minusc}")
