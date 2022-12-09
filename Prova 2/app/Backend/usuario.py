from dataclasses import dataclass, field
from typing import List
from app.Backend.pessoa import Pessoa

# Cria a super classe Filme

@dataclass
class Usuario(Pessoa):
    login: str = "-"
    senha: str = "-"
    email: str = "-"
    telefone: str = "-"
    endereco: str = "-"

    def __eq__(self, other):
        return self.login == other.login or self.email == other.email