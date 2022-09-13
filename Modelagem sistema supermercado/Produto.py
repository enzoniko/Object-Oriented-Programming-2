class Produto:
    def __init__(self, nome, tipo, preco):
        self.id = id(self)
        self.nome = nome
        self.tipo = tipo
        self.preco = preco

    def get_id(self):
        return self.id

    def get_nome(self):
        return self.nome

    def get_tipo(self):
        return self.tipo

    def get_preco(self):
        return self.preco

    def set_nome(self):
        self.nome = nome

    def set_tipo(Self):
        self.tipo = tipo

    def set_preco(self):
        self.preco = preco


LISTA = [("Maça", "Frutas", 3.50), ("Batata Frita", 'Frios', 12.00), ("Lasanha congelada", 'Frios', 10.00), ("Pizza", "Frios", 15.00), ("Banana", "Frutas", 4.00), ("Tomate", "Frutas", 2.00), ("Pepino", "Legumes e Verduras", 2.00), ("Brocolis", "Legumes e Verduras",
                                                                                                                                                                                                                                        4.00), ("Pão de Queijo", "Padaria", 5.00), ("Bolo de Cenoura", "Padaria", 7.00), ("Pão de trigo", "Padaria", 4.00), ("Maminha", "Carnes", 19.00), ("Carne Moida", "Carnes", 14.00), ("Contra Filé", "Carnes", 20.00), ("Papel Higiênico", "Higiene e Limpeza", 5.00), ("Sabão em Pó", "Higiene e Limpeza", 8.00), ("Detergente", "Higiene e Limpeza", 3.00)]
PRODUTOS = [Produto(produto[0], produto[1], produto[2]) for produto in LISTA]
