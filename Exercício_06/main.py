import sys

# lê os valores Min e Máx
entrada = sys.stdin.read().strip().split()
minimo = int(entrada[0])
maximo = int(entrada[1])

primos = []

# percorre todos os números no intervalo
for n in range(minimo, maximo + 1):
    if n > 1:  # números primos são maiores que 1
        eh_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos.append(str(n))

# saída
if primos:
    print(" ".join(primos))
else:
    print("Não há números primos")
