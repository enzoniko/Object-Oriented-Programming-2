from Produto import *


class Carrinho:
    def __init__(self):
        self.id = id(self)
        self.itens = {}
        self.produtos = []

    def get_id(self):
        return self.id

    def get_produtos(self):
        return self.produtos

    def set_produtos(self, produtos):
        self.produtos = produtos
        return

    def adicionar_produtos(self, produto, quantidade):
        self.itens[produto.get_nome()] = quantidade
        self.produtos.append(produto) if produto not in self.produtos else None
        return

    def remover_produtos(self, produto, quantidade):
        self.itens[produto.get_nome()] -= quantidade
        if self.itens[produto.get_nome()] == 0:
            self.produtos.remove(produto)
            self.itens.pop(produto.get_nome())
        return

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += self.itens[produto.get_nome()] * produto.get_preco()
        return total

    def printar_produtos(self):
        if len(self.produtos) == 0:
            print("Carrinho vazio!")
            return
        else:
            print("Produto:----------------------------------------------Preço:")
            for produto in self.produtos:
                print(
                    f"{self.itens[produto.get_nome()]}x {produto.get_nome()}------------------------------------------ R$ {self.itens[produto.get_nome()] * produto.get_preco()}")
            print()
            print(f"Total:  R$ {self.calcular_total()}")
            return


# carro = Carrinho()
# carro.adicionar_produtos(PRODUTOS[0], 2)
# carro.adicionar_produtos(PRODUTOS[1], 1)
# carro.printar_produtos()
