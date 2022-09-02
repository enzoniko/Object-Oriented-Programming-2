from Produto import *
from Carrinho import *


def deseja_continuar(funcao, *args):
    continuar = input("Deseja continuar? (S/N): ")
    while continuar.upper() not in ["S", "N"]:
        continuar = input("Digite uma opção válida: ")
    if continuar.upper() == "N":
        return
    else:
        return funcao(*args)


def opcao_desejada(limite, coisa="opção"):
    print()
    result = int(input(f"Digite a {coisa} desejada: "))
    while result > limite:
        result = int(input(f"Digite uma {coisa} válida: "))
    return result


def adicionar_produtos(carrinho):
    print("Que tipo de produto você deseja comprar?")
    tipos = list({elemento[1] for elemento in LISTA})
    for indice, tipo in enumerate(tipos):
        print(f"{indice + 1} - {tipo}")

    opcao = opcao_desejada(len(tipos))
    produtos = [elemento for elemento in LISTA if elemento[1]
                == tipos[opcao - 1]]

    for indice, produto in enumerate(produtos):
        print(f"{indice + 1} - {produto[0]}")

    carrinho.adicionar_produtos(
        PRODUTOS[LISTA.index(produtos[opcao_desejada(len(produtos)) - 1])], int(input("Digite a quantidade desejada: ")))

    carrinho.printar_produtos()

    deseja_continuar(adicionar_produtos, carrinho)
    return


def remover_produtos(carrinho):
    produtos = carrinho.get_produtos()
    if produtos == []:
        print("Carrinho vazio!")
        return
    carrinho.printar_produtos()

    print("Que produto você deseja remover?")
    for indice, produto in enumerate(produtos):
        print(f"{indice + 1} - {produto.get_nome()}")
    print()
    produto = opcao_desejada(len(produtos))

    carrinho.remover_produtos(produtos[produto - 1], opcao_desejada(
        carrinho.itens[produtos[produto - 1].get_nome()], "quantidade"))

    carrinho.printar_produtos()

    deseja_continuar(remover_produtos, carrinho)
    return


def main():
    print("Bem vindo!")
    carrinho = Carrinho()
    while True:
        print("1 - Adicionar produto ao carrinho")
        print("2 - Remover produto do carrinho")
        print("3 - Ver carrinho")
        print("4 - Finalizar compra")
        opcao = int(input("Digite a opção desejada: "))
        while opcao not in [1, 2, 3, 4]:
            opcao = int(input("Digite uma opção válida: "))
        if opcao == 1:
            adicionar_produtos(carrinho)
        elif opcao == 2:
            remover_produtos(carrinho)
        elif opcao == 3:
            carrinho.printar_produtos()
        elif opcao == 4:
            carrinho.printar_produtos()
            print("Compra finalizada! Volte sempre!")
            break
    return


if __name__ == "__main__":
    main()
