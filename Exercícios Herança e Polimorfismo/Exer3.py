class Imovel():
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    def getEndereco(self):
        return self.endereco

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco


class Novo(Imovel):
    def __init__(self, endereco, preco, adicional):
        super().__init__(endereco, preco)
        self.adicional = adicional

    def getAdicional(self):
        return self.adicional

    def setAdicional(self, adicional):
        self.adicional = adicional

    def imprimeValor(self):
        print("Valor do imóvel: R$ %.2f" % self.preco)
        print("Valor do adicional: R$ %.2f" % self.adicional)
        print("Valor total: R$ %.2f" % (self.preco + self.adicional))


class Velho(Imovel):
    def __init__(self, endereco, preco, desconto=0.15):
        super().__init__(endereco, preco)
        self.desconto = desconto

    def getDesconto(self):
        return self.desconto

    def setDesconto(self, desconto):
        self.desconto = desconto

    def imprimeValor(self):
        print("Valor do imóvel: R$ %.2f" % self.preco)
        print(f"Valor do desconto: R$ {str(self.desconto[2:])}%")
        print("Valor total: R$ %.2f" % (self.preco - self.preco*self.desconto))
