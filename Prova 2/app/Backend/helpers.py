# Importar Pickle para salvar e carregar objetos
import pickle
from typing import List

# Função lista_strings_para_string: recebe uma lista de strings e retorna uma string com todas as strings separadas por vírgula
def lista_strings_para_string(lista) -> str:
    return ", ".join(lista)

# Helper functions for the database:
def save_object(obj: callable, filename: str):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_object(filename: str) -> callable:
    with open(filename, 'rb') as input:
        return pickle.load(input)

def save_objects(objs: list, filename: str):
    with open(filename, 'wb') as output:
        for obj in objs:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def load_objects(filename: str):
    with open(filename, 'rb') as input:
        while True:
            try:
                yield pickle.load(input)
            except EOFError:
                break

def store_objects(objs: list, filename: str) -> List[callable]:
    save_objects(objs, filename)
    return list(load_objects(filename))

def update_objects(new_objs: list, filename: str) -> List[callable]:
    old_objects = list(load_objects(filename))
    old_objects.extend(new_objs)
    save_objects(old_objects, filename)
    return list(load_objects(filename))
