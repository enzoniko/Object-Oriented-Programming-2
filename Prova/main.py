from Classes import *
# Lista de clientes
clientes: list[Cliente] = []
# Livros disponíveis
estoque: Estoque = Estoque()

# Função principal
def main():
    
    print("----------------------------------------------")
    print("Bem vindo à livraria comunitária!")
    print("----------------------------------------------")
    while True:
        # Entrar no sistema
        cliente = entrar()

        # Menu (emprestar, pegar emprestado, ver livros)
        while menu(cliente) != 0:
            pass

# Função que faz quase todas as operações do sistema         
def menu(cliente: Cliente) -> 0|1:
    print_menu("---------------------------------------", "Digite 1 para emprestar um livro:", "Digite 2 para pegar um livro emprestado:", "Digite 3 pra ver seus livros:", "Digite 0 para sair:", "---------------------------------------")

    # Pegar a opção do usuário
    opcao: int = int(input())
    while opcao not in [1, 2, 3, 0]:
        print_menu("---------------------------------------", "Digite 1 para emprestar um livro:", "Digite 2 para pegar um livro emprestado:", "Digite 3 pra ver seus livros:", "Digite 0 para sair:", "---------------------------------------")

        opcao: int = int(input("=> "))

    # Emprestar um livro
    if opcao == 1:
        livro = get_livro_info()
        if livro in estoque.livros.keys():
            print("Livro já cadastrado!")

        else:
            print("Digite a quantidade de livros:")
            quantidade: int = int(input("=> "))
            # Adicionar o livro ao estoque
            estoque.adicionarLivros(livro, quantidade)
        return 1

    # Pegar um livro emprestado
    elif opcao == 2:
        livro = get_livro_info()
        # Verificar se o livro está disponível
        if livro in estoque.livros.keys() and estoque.livros[livro] > 0:
            print("Digite a quantidade de livros:")
            quantidade: int = int(input("=> "))
            # Verificar se a quantidade de livros é válida
            while quantidade > estoque.livros[livro]:
                print(f"Temos apenas {estoque.livros[livro]} livros disponíveis!")
                print("Digite a quantidade de livros:")
                quantidade: int = int(input("=> "))

            # Adicionar o livro ao cliente
            cliente.adicionarLivro(livro, quantidade)
            # Remover o livro do estoque
            estoque.removerLivros(livro, quantidade)
        else:
            print("Livro não cadastrado!")

        return 1
    
    # Ver os livros do cliente
    elif opcao == 3:
        # Printar os livros do cliente
        if cliente.livros == []:
            print("Você não tem livros emprestados!")
        cliente.printLivros()
        return 1
    
    # Sair do menu
    else:
        return 0

# Função que exibe o menu principal
def print_menu(*args) -> None:
    for arg in args:
        print(arg)

# Função que pega as informações do livro
def get_livro_info() -> Livro:
    print("Digite o titulo do livro:")
    titulo: str = input("=> ")
    print("Digite o autor do livro:")
    autor: str = input("=> ")
    print("Digite a categoria do livro:")
    categoria: str = input("=> ")
    return Livro(titulo, autor, categoria)

# Função que faz a operação de entrar no sistema
def entrar() -> Cliente:
    print("Digite 1 para se registrar ou 2 para fazer login:")
    opcao: int = int(input("=> "))
    while opcao not in [1, 2]:
        print("Digite 1 para se registrar ou 2 para fazer login:")
        opcao: int = int(input("=> "))
    
    # Registro
    if opcao == 1:
        
        cliente: Cliente|None = registro()

    # Login     
    else:
        while True:
            cliente: Cliente|None = login()
            if cliente is not None:
                break
    return cliente

# Função que faz a operação de registro no sistema
def registro() -> Cliente:
    print("Digite seu nome:")
    nome: str = input("=> ")
    print("Digite seu telefone:")
    telefone: str = input("=> ")
    print("Digite seu email:")
    email: str = input("=> ")
    cliente: Cliente = Cliente(nome, telefone, email)
    # Verifica se ele ja não esta cadastrado
    if cliente in clientes:
        print("Você já está registrado!")
        return entrar()
    print("Digite sua senha:")
    senha: str = input("=> ")
    cliente.set_senha(senha)
    print("Registro realizado com sucesso!")
    # Cadastrar o cliente
    clientes.append(cliente)
    return cliente

# Função que faz a operação de login no sistema
def login() -> Cliente|None:
    print("Digite seu email:")
    email: str = input("=> ")
    print("Digite sua senha:")
    senha: str = input("=> ")
    # Verifica se a senha está correta
    for cliente in clientes:
        if cliente.email == email and cliente.get_senha() == senha:
            print("Login realizado com sucesso!")
            return cliente
    print("Login inválido! Tem certeza que está registrado?")
    return None

# Chama a função principal	
if __name__ == "__main__":
    main()