import sys

def balanceado(s, contador=0):
    # caso base: string vazia
    if not s:
        return contador == 0
    # se o contador ficar negativo, já está desbalanceado
    if contador < 0:
        return False
    # passo recursivo: verifica o primeiro caractere e chama para o restante
    if s[0] == "(":
        return balanceado(s[1:], contador + 1)
    elif s[0] == ")":
        return balanceado(s[1:], contador - 1)
    else:
        # se aparecer caractere inválido
        return balanceado(s[1:], contador)

# lê a entrada
entrada = sys.stdin.read().strip()

# imprime True ou False
print(balanceado(entrada))
