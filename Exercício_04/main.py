import sys

# Lê todos os números da entrada
dados = list(map(int, sys.stdin.read().split()))

# Primeira matriz (2x2)
a11, a12, a21, a22 = dados[0], dados[1], dados[2], dados[3]

# Segunda matriz (2x2)
b11, b12, b21, b22 = dados[4], dados[5], dados[6], dados[7]

# Cálculo da matriz resultante
c11 = a11 * b11 + a12 * b21
c12 = a11 * b12 + a12 * b22
c21 = a21 * b11 + a22 * b21
c22 = a21 * b12 + a22 * b22

# Impressão no formato pedido
print(f"{c11} {c12}")
print(f"{c21} {c22}")
