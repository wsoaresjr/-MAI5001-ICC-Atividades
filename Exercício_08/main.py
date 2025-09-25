import sys

# lê a string da entrada
texto = sys.stdin.read().strip().lower()

# divide em palavras (simples, separadas por espaço)
palavras = texto.split()

# dicionário para guardar frequências
frequencias = {}

# percorre os pares consecutivos
for i in range(len(palavras) - 1):
    bigrama = palavras[i] + " " + palavras[i+1]
    if bigrama in frequencias:
        frequencias[bigrama] += 1
    else:
        frequencias[bigrama] = 1

# imprime cada bigrama e sua contagem
for bigrama, qtd in frequencias.items():
    print(f"{bigrama}: {qtd}")
