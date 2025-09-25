import sys

entrada = sys.stdin.read().strip()

partes = entrada.split(":")
horas = int(partes[0])
minutos = int(partes[1])
segundos = int(partes[2])

total_segundos = horas * 3600 + minutos * 60 + segundos

# imprime exatamente como esperado, sem newline no final
print(total_segundos, end="")
