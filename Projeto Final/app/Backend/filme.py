# Importa a função lista_strings_para_string do módulo helpers
from dataclasses import dataclass, field
from app.Backend.helpers import lista_strings_para_string, automatic_getters_and_setters

# Importa a função lista_strings_para_string do módulo helpers
# from helpers import lista_strings_para_string

# Cria a super classe Filme

@automatic_getters_and_setters
@dataclass
class Filme:
    _nome: str = ""
    _generos: list[str] = field(default_factory=list)
    imagem: str = ""

    # print_info imprime os informações do filme
    def print_info(self):
        print(self.nome, end=" (")
        print(lista_strings_para_string(self.generos), end=")\n")

f = Filme("O Poderoso Chefão", ["Drama", "Crime"], "https://www.imdb.com/title/tt0068646/mediaviewer/rm1776027136")
f.print_info()