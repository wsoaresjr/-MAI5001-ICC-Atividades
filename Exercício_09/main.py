import sys

# lê os valores Min e Max
entrada = sys.stdin.read().strip().split()
minimo = int(entrada[0])
maximo = int(entrada[1])

perfeitos = []

# percorre o intervalo
for n in range(minimo, maximo + 1):
    if n > 1:
        soma_divisores = 0
        for i in range(1, n):
            if n % i == 0:
                soma_divisores += i
        if soma_divisores == n:
            perfeitos.append(n)

# saída
if perfeitos:
    for p in perfeitos:
        print(p)
else:
    print("Não foi encontrado número perfeito")

