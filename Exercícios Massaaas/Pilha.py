class Pilha():
    def __init__(self):
        self.pilha = []

    def empilhar(self, valor):
        self.pilha.append(valor)

    def desempilhar(self):
        return self.pilha.pop()

    def vazia(self):
        return len(self.pilha) == 0

    def topo(self):
        return self.pilha[-1]


class Pilha_filha(Pilha):
    def __init__(self):
        super().__init__()

    def desempilhar(self):
        return None if self.vazia() else super().desempilhar()


if __name__ == '__main__':
    pilha = Pilha()
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    pilha.empilhar(4)
    pilha.empilhar(5)
    print(pilha.desempilhar())
    print(pilha.desempilhar())
    print(pilha.desempilhar())
    print(pilha.desempilhar())
