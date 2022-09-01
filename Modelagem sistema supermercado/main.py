from Produto import *
from Carrinho import *


def main():
    print("Bem vindo!")
    carrinho = Carrinho()
    while True:
        print("Que tipo de produto você deseja comprar?")
        tipos = {elemento[1] for elemento in LISTA}
        tipos = list(tipos)
        for indice, tipo in enumerate(tipos):
            print(f"{indice + 1} - {tipo}")

        print("0 - Sair")
        print()
        tipo = int(input("Digite a opção desejada: "))
        while tipo > len(tipos):
            tipo = int(input("Digite uma opção válida: "))
        if tipo == 0:
            print("Programa encerrado!")
            break
        else:
            produtos = [
                elemento for elemento in LISTA if elemento[1] == tipos[tipo - 1]]
            for indice, produto in enumerate(produtos):
                print(f"{indice + 1} - {produto[0]}")

            print()
            produto = int(input("Digite a opção desejada: "))
            while produto > len(produtos):
                produto = int(input("Digite uma opção válida: "))
            if produto == 0:
                print("Programa encerrado!")
                break
            else:
                quantidade = int(input("Digite a quantidade desejada: "))
                carrinho.adicionar_produtos(
                    PRODUTOS[LISTA.index(produtos[produto - 1])], quantidade)
                carrinho.printar_produtos()
                continuar = input("Deseja continuar comprando? (S/N): ")
                while continuar.upper() not in ["S", "N"]:
                    continuar = input("Digite uma opção válida: ")
                if continuar.upper() == "N":
                    print("Programa encerrado!")
                    break
                else:
                    continue


if __name__ == "__main__":
    main()
