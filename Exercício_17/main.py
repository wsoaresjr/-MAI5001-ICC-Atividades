import sys

class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)


# lê a entrada
dados = sys.stdin.read().strip().split()
largura = float(dados[0])
altura = float(dados[1])

# cria objeto da classe Retangulo
ret = Retangulo(largura, altura)

# imprime resultados formatados
print(f"Área: {ret.calcular_area()}")
print(f"Perímetro: {ret.calcular_perimetro():.1f}")
