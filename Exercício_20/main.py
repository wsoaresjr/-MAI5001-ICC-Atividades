import sys

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_bonus(self):
        return self.salario * 0.10

    def salario_com_bonus(self):
        return self.salario + self.calcular_bonus()


class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento

    def calcular_bonus(self):
        return self.salario * 0.20


# lê os dados da entrada
dados = sys.stdin.read().strip().splitlines()

# funcionário
nome_func = dados[0]
salario_func = float(dados[1])
funcionario = Funcionario(nome_func, salario_func)

# gerente
nome_ger = dados[2]
salario_ger = float(dados[3])
departamento = dados[4]
gerente = Gerente(nome_ger, salario_ger, departamento)

# saída
print(f"{funcionario.nome}: Salário com bônus = {funcionario.salario_com_bonus():.1f}")
print(f"{gerente.nome}: Salário com bônus = {gerente.salario_com_bonus():.1f}")
