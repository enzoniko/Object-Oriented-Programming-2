class Ingresso():
    def __init__(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def imprimeValor(self):
        print("Valor do ingresso: R$ %.2f" % self.valor)


class IngressoVIP(Ingresso):
    def __init__(self, valor, adicional):
        super().__init__(valor)
        self.adicional = adicional

    def getAdicional(self):
        return self.adicional

    def setAdicional(self, adicional):
        self.adicional = adicional

    def imprimeValor(self):
        super().imprimeValor()
        print("Valor do adicional: R$ %.2f" % self.adicional)
        print("Valor total: R$ %.2f" % (self.valor + self.adicional))


class Normal(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def imprimeIngressoNormal(self):
        print("Ingresso Normal")
        super().imprimeValor()


class CamaroteInferior(IngressoVIP):
    def __init__(self, valor, adicional, local):
        super().__init__(valor, adicional)
        self.local = local

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local

    def imprimeLocal(self):
        print("Local: ", self.local)
        super().imprimeValor()


class CamaroteSuperior(IngressoVIP):
    def __init__(self, valor, adicional, local, adicional2=50):
        self.adicional2 = adicional2
        # Inheritance overloading parameters error???
        super().__init__(valor, adicional, local)

    def getLocal(self):
        return self.local

    def setLocal(self, local):
        self.local = local

    def getAdicional2(self):
        return self.adicional2

    def setAdicional2(self, adicional2):
        self.adicional2 = adicional2

    def imprimeLocal(self):
        print("Local: ", self.local)
        super().imprimeValor()

    def imprimeValor(self):
        super().imprimeValor()
        print("Valor do adicional 2: R$ %.2f" % self.adicional2)
        print("Valor total: R$ %.2f" %
              (self.valor + self.adicional + self.adicional2))
