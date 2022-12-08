from dataclasses import dataclass, field
from typing import List

# Cria a super classe Filme

@dataclass
class Pessoa:
    nome: str = "-"
    sobrenome: str = "-"
    idade: int = 0
    genero: str = "-"
    cpf: str = "-"