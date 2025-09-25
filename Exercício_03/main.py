import sys

texto = sys.stdin.read().strip()

# dicionário para guardar frequências
frequencias = {}

# percorre cada caractere e conta
for c in texto:
    if c in frequencias:
        frequencias[c] += 1
    else:
        frequencias[c] = 1

# imprime cada caractere e sua contagem
for caractere, qtd in frequencias.items():
    print(f"{caractere}: {qtd}")
