import sys

texto = sys.stdin.read().strip()

# Aceita "a b" ou "a,b" (com ou sem espaços)
texto = texto.replace(",", " ")
partes = [p for p in texto.split() if p]

# Garante que existam dois números
minimo = int(partes[0])
maximo = int(partes[1])

# Caso venham invertidos (ex.: "200 100"), troca
if minimo > maximo:
    minimo, maximo = maximo, minimo

# Coleta os números divisíveis por 7 e múltiplos de 5 (i.e., múltiplos de 35)
nums = []
for n in range(minimo, maximo + 1):
    if n % 7 == 0 and n % 5 == 0:
        nums.append(str(n))

# Imprime em CSV, sem quebra de linha final
print(",".join(nums), end="")

