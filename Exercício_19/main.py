import sys

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        # caso contrário, não faz nada (saldo não pode ficar negativo)


# lê os dados da entrada
dados = sys.stdin.read().strip().splitlines()

titular = dados[0]
saldo_inicial = float(dados[1])
deposito = float(dados[2])
saque = float(dados[3])

# cria objeto da conta bancária
conta = ContaBancaria(titular, saldo_inicial)

# processa operações
conta.depositar(deposito)
conta.sacar(saque)

# imprime saldo final com 1 casa decimal
print(f"Saldo final: {conta.saldo:.1f}")
