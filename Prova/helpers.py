from functools import partial

# Função que criei pra automatizar o processo de getters e setters
# Funciona como um decorador, você bota ele em uma classe e todos os atributos que tiverem '-' no começo do nome, vão ter um getter e um setter criado automaticamente
def automatic_getters_and_setters(original_class):
    privateatributeslist = [name for name, _ in original_class.__dict__.items() if name.startswith("_") and not name.startswith("__")]

    for name in privateatributeslist:
        setattr(original_class, f'get{name}', classmethod(partial(lambda cls, name: getattr(cls, name), name=name)))
        setattr(original_class, f'set{name}', classmethod(partial(lambda cls, value, name: setattr(cls, name, value), name=name)))

    return original_class