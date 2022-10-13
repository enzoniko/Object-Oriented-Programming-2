from pessoa import Pessoa
from dataclasses import dataclass, field
from random import randint
from helpers import automatic_getters_and_setters

@automatic_getters_and_setters
@dataclass
class Cliente(Pessoa):
    id: int = field(default = id(randint(0, 1000000)))
    _compras: list = field(default_factory = list)
   
    def add_compra(self, compra):
        self._compras.append(compra)
    
    def print_info(self):
        super().print_info()
        print("ID: ", self.id)
        print("Compras: ", self._compras)
    
for name, value in Cliente.__dict__.items():
    if not name.startswith('__'):
        print(name, value)
c1 = Cliente(20, 12345678900)
c1.print_info()
c1.add_compra('Compra 1')
"""
why isn't the @automatic_getters_and_setters decorator working? I'm getting the following error:
AttributeError: 'Cliente' object has no attribute 'set_compras'. Did you mean: '_compras'?
"""

c1.set_compras(['Compra 1', 'Compra 2'])
c1.print_info()

