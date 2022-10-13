from dataclasses import dataclass, field
from helpers import automatic_getters_and_setters

# Classe Pessoa
@dataclass
class Pessoa:
    nome: str 
    telefone: str 
    email: str 

# Classe Livro
@dataclass(unsafe_hash=True)
class Livro:
    titulo: str = 'Titulo'
    autor: str = 'Autor'
    categoria: str = 'Categoria'

    # Representa os livros bonitinhos
    def __repr__(self):
        return f'{self.titulo} - {self.autor} - {self.categoria}'

# Classe Cliente
@automatic_getters_and_setters
@dataclass
class Cliente(Pessoa):
    # Senha é o único atributo que não é público
    _senha: str = field(init=False, default=False)
    livros: list[Livro] = field(init=False, default_factory=list)

    # Função que adiciona um livro na lista de livros do cliente
    def adicionarLivro(self, livro: Livro, quantidade: int) -> None:
        for _ in range(quantidade):
            self.livros.append(livro)

    # Função que printa os livros do cliente
    def printLivros(self) -> None:
        for livro in self.livros:
            print(livro)
            print()

# Classe Estoque
@dataclass
class Estoque:
    livros: dict[Livro, int] = field(default_factory=dict)
     
    # Função que adiciona livros ao estoque
    def adicionarLivros(self, livro: Livro, quantidade: int) -> None:
        self.livros[livro] = quantidade if livro not in self.livros else self.livros[livro] + quantidade

    # Função que remove livros do estoque
    def removerLivros(self, livro: Livro, quantidade: int) -> None:
        self.livros[livro] = self.livros[livro] - quantidade if livro in self.livros else 0
        if self.livros[livro] == 0:
            del self.livros[livro]
    
