import sys

def valores_unicos(lista):
    # compara o tamanho da lista com o tamanho do conjunto
    return len(lista) == len(set(lista))

# lê a entrada
entrada = sys.stdin.read().strip().split()

# converte cada elemento para inteiro
numeros = list(map(int, entrada))

# chama a função
print(valores_unicos(numeros))

