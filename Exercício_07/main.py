import sys

# lê três inteiros da entrada
valores = list(map(int, sys.stdin.read().split()))

# calcula a média
media = sum(valores) / 3

# imprime arredondado para 1 casa decimal
print(f"{media:.1f}")
