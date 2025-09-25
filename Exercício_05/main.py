import sys
import re

# lê a string de entrada
texto = sys.stdin.read().strip().lower()

# mantém apenas letras e espaços (remove pontuações)
texto = re.sub(r'[^a-zá-úà-ùãõâêîôûç\s]', ' ', texto)

# separa em palavras
palavras = texto.split()

# dicionário de frequências
frequencias = {}

for palavra in palavras:
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1

# imprime cada palavra e sua contagem
for palavra, qtd in frequencias.items():
    print(f"{palavra}: {qtd}")
