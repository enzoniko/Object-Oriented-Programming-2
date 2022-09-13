from functools import lru_cache


class Exercises:
    def __init__(self, exercise):
        getattr(self, f'exer_{str(exercise)}')()
        return

    def exer_1(self):
        # Exercício 1
        # Faça um programa que peça uma nota, entre zero e dez.
        # Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
        nota = int(input("Digite uma nota entre 0 e 10: "))
        while nota < 0 or nota > 10:
            print("Nota inválida")
            nota = int(input("Digite uma nota entre 0 e 10: "))
        print("Nota válida!")
        return

    def exer_2(self):
        # Exercício 2
        # Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
        # mostrando uma mensagem de erro e voltando a pedir as informações.
        nome = input("Digite seu nome: ")
        senha = input("Digite sua senha: ")
        while senha == nome:
            print("Senha inválida, digite uma senha diferente do nome")
            nome = input("Digite seu nome: ")
            senha = input("Digite sua senha: ")
        print("Senha válida!")
        return

    def exer_3(self):
        # Exercício 3
        # Faça um programa que leia e valide as seguintes informações:
        # a. Nome: maior que 3 caracteres;
        # b. Idade: entre 0 e 150;
        # c. Salário: maior que zero;
        # d. Sexo: 'f' ou 'm';
        # e. Estado Civil: 's', 'c', 'v', 'd'
        nome = input("Digite seu nome: ")
        while len(nome) <= 3:
            print("Nome inválido, digite um nome com mais de 3 caracteres")
            nome = input("Digite seu nome: ")

        idade = int(input("Digite sua idade: "))
        while idade < 0 or idade > 150:
            print("Idade inválida, digite uma idade entre 0 e 150")
            idade = int(input("Digite sua idade: "))

        salario = float(input("Digite seu salário: "))
        while salario <= 0:
            print("Salário inválido, digite um salário maior que 0")
            salario = float(input("Digite seu salário: "))

        sexo = input("Digite seu sexo: (m/f) ")
        while sexo not in ["f", "m"]:
            print("Sexo inválido, digite 'f' para feminino ou 'm' para masculino")
            sexo = input("Digite seu sexo: ")

        estado_civil = input("Digite seu estado civil: (s/c/v/d) ")
        while estado_civil not in ["s", "c", "v", "d"]:
            print("Estado civil inválido, digite 's' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado")
            estado_civil = input("Digite seu estado civil: ")
        print("Dados válidos!")
        return

    def exer_4(self):
        # Exercício 4
        # Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
        # anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa
        # de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos
        # necessários para que a população do país A ultrapasse ou iguale a população do país B,
        # mantidas as taxas de crescimento.
        populacao_a = 80000
        populacao_b = 200000
        taxa_a = 0.03
        taxa_b = 0.015
        anos = 0
        while populacao_a < populacao_b:
            populacao_a += (populacao_a * taxa_a)
            populacao_b += (populacao_b * taxa_b)
            anos += 1
        print("Número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B: ", anos)
        return

    def exer_5(self):
        # Exercício 5
        # Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
        # crescimento iniciais. Valide a entrada e permita repetir a operação.
        while True:
            populacao_a = int(input("Digite a população do país A: "))
            populacao_b = int(input("Digite a população do país B: "))
            taxa_a = float(input("Digite a taxa de crescimento do país A: "))
            taxa_b = float(input("Digite a taxa de crescimento do país B: "))

            while populacao_a <= 0 or populacao_b <= 0 or taxa_a <= 0 or taxa_b <= 0:
                print("População ou taxa inválida, digite valores positivos")
                populacao_a = int(input("Digite a população do país A: "))
                populacao_b = int(input("Digite a população do país B: "))
                taxa_a = float(
                    input("Digite a taxa de crescimento do país A: "))
                taxa_b = float(
                    input("Digite a taxa de crescimento do país B: "))

            anos = 0
            while populacao_a < populacao_b:
                populacao_a += (populacao_a * taxa_a)
                populacao_b += (populacao_b * taxa_b)
                anos += 1

            print("Número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B: ", anos)
            if input("Deseja continuar? (s/n) ").lower() == "n":
                print("Fim do programa")
                break
        return

    def exer_6(self):
        # Exercício 6
        # Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois
        # modifique o programa para que ele mostre os números um ao lado do outro.
        for i in range(1, 21):
            print(i)

        for i in range(1, 21):
            print(i, end=" ")
        return

    def exer_7(self):
        # Exercício 7
        # Faça um programa que leia 5 números e informe o maior número
        numeros = [int(input("Digite um número: ")) for _ in range(5)]
        print("O maior número é: ", max(numeros))
        return

    def exer_8(self):
        # Exercício 8
        # Faça um programa que leia 5 números e informe a soma e a média dos números.
        numeros = [int(input("Digite um número: ")) for _ in range(5)]
        print("Soma: ", sum(numeros))
        print("Média: ", sum(numeros) / len(numeros))
        return

    def exer_9(self):
        # Exercício 9
        # Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
        for i in range(1, 51):
            if i % 2 == 1:
                print(i)
        return

    def exer_10(self):
        # Exercício 10
        # Faça um programa que receba dois números inteiros e gere os números inteiros que estão
        # no intervalo compreendido por eles.
        print([i for i in range(int(input("Digite o primeiro número: ")),
              int(input("Digite o segundo número: ")) + 1)])
        return

    def exer_11(self):
        # Exercício 11
        # Altere o programa anterior para mostrar no final a soma dos números.
        print(sum([i for i in range(int(input("Digite o primeiro número: ")), int(
            input("Digite o segundo número: ")) + 1)]))
        return

    def exer_12(self):
        # Exercício 12
        # Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
        # entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve
        # ser conforme o exemplo abaixo:
        # Tabuada de 5:
        # 5 X 1 = 5
        # 5 X 2 = 10
        # ...
        # 5 X 10 = 50
        numero = int(input("Digite um número: "))
        while numero < 1 or numero > 10:
            print("Número inválido, digite um número entre 1 e 10")
            numero = int(input("Digite um número: "))
        for i in range(1, 11):
            print(numero, " X ", i, " = ", numero * i)
        return

    def exer_13(self):
        # Exercício 13
        # Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
        # número elevado ao segundo número. Não utilize a função de potência da linguagem.
        base = int(input("Digite a base: "))
        expoente = int(input("Digite o expoente: "))
        numero_final = 1
        for _ in range(expoente):
            numero_final *= base
        print("O resultado da potenciação é: ", numero_final)
        return

    def exer_14(self):
        # Exercício 14
        # Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
        # números pares e a quantidade de números impares.
        numeros = [int(input("Digite um número: ")) for _ in range(10)]
        print("Quantidade de números pares: ", len(
            [x for x in numeros if x % 2 == 0]))
        print("Quantidade de números ímpares: ", len(
            [x for x in numeros if x % 2 == 1]))
        return

    @lru_cache(maxsize=None)
    def fib(self, n):
        return (n if n < 2 else self.fib(n-1) + self.fib(n-2))

    def exer_15(self):
        # Exercício 15
        # A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um
        # programa capaz de gerar a série até o n−ésimo termo.
        numero = int(input("Digite um número: "))
        for i in range(1, numero + 1):
            print(self.fib(i), end=" ")
        print()
        return

    def exer_16(self):
        # Exercício 16
        # A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um
        # programa que gere a série até que o valor seja maior que 500.
        i = 0
        while True:
            fibonnaci = self.fib(i)
            if fibonnaci > 500:
                break
            print(fibonnaci, end=" ")
            i += 1
        print()
        return

    @lru_cache(maxsize=None)
    def fat(self, n):
        return (n if n < 2 else n * self.fat(n-1))

    def exer_17(self):
        # Exercício 17
        # Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
        # Ex.: 5!=5.4.3.2.1=120
        print(f"Fatorial: {self.fat(int(input('Digite um número: ')))}")
        return

    def exer_18(self):
        # Exercício 18
        # Faça um programa que, dado um conjunto de N números, determine o menor valor, o
        # maior valor e a soma dos valores.
        numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(
            int(input("Digite a quantidade de números: ")))]
        print("Maior número: ", max(numeros))
        print("Menor número: ", min(numeros))
        print("Soma dos números: ", sum(numeros))
        return

    def exer_19(self):
        # Exercício 19
        # Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
        numeros = []
        for i in range(int(input("Digite a quantidade de números: "))):
            numero = int(input(f"Digite o {i + 1}º número: "))
            while numero < 0 or numero > 1000:
                print("Número inválido, digite um número entre 0 e 1000")
                numero = int(input(f"Digite o {i + 1}º número: "))
            numeros.append(numero)
        # numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(
        #     int(input("Digite a quantidade de números: ")))]
        # while numeros != [x for x in numeros if x >= 0 and x <= 1000]:
        #     print("Digite apenas números entre 0 e 1000!!")
        #     numeros = [int(input(f"Digite o {i + 1}º número: ")) for i in range(
        #         int(input("Digite a quantidade de números: ")))]
        print("Maior número: ", max(numeros))
        print("Menor número: ", min(numeros))
        print("Soma dos números: ", sum(numeros))
        return

    def exer_20(self):
        # Exercício 20
        # Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias
        # vezes e limitando o fatorial a números inteiros positivos e menores que 16.
        while True:
            numero = int(input("Digite um número: "))
            if numero < 0 or numero > 16:
                print("Número inválido, digite um número entre 0 e 16")
                continue
            print(f"Fatorial de {numero}: {self.fat(numero)}")
            if input("Deseja continuar? (s/n) ").lower() == "n":
                break
        return

    def primo(self, p):

        multiplos = sum(p % x == 0 for x in range(2, p))
        return multiplos == 0

    def exer_21(self):

        # Exercício 21
        # Faça um programa que peça um número inteiro e determine se ele é ou não um número
        # primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
        numero = int(input("Digite um número: "))
        primo = self.primo(numero)
        print(
            f"O número {numero} é primo" if primo else f"O número {numero} não é primo")
        return

    def divisores(self, n):
        return [x for x in range(1, n + 1) if n % x == 0]

    def exer_22(self):
        # Exercício 22
        # Altere o programa de cálculo dos números primos, informando, caso o número não seja
        # primo, por quais número ele é divisível.
        numero = int(input("Digite um número: "))
        primo = self.primo(numero)
        print(
            f"O número {numero} é primo" if primo else f"O número {numero} não é primo, os divisores dele são: \n{self.divisores(numero)}")
        return

    def exer_23(self):
        # Exercício 23
        # Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro
        # fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele
        # executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o
        # número de testes (divisões) executados.
        numero = int(input("Digite um número: "))
        primos = [x for x in range(1, numero + 1) if self.primo(x)]
        print(f"Os números primos entre 1 e {numero} são: \n{primos}")
        print(
            f"Número de divisões necessárias: {sum(x - 2 for x in range(1, numero + 1))}")
        return

    def exer_24(self):
        # Exercício 24
        # Faça um programa que calcule o mostre a média aritmética de N notas.
        notas = [float(input(f"Digite a {i + 1}º nota: "))
                 for i in range(int(input("Digite a quantidade de notas: ")))]
        print(f"Média: {sum(notas) / len(notas)}")
        return

    def exer_25(self):
        # Exercício 25
        # Faça um programa que peça para n pessoas a sua idade, ao final o programa devera
        # verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então,
        # dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
        idades = [int(input(f"Digite a idade da {i + 1}º pessoa: "))
                  for i in range(int(input("Digite a quantidade de pessoas: ")))]
        media = sum(idades) / len(idades)
        if media >= 0 and media <= 25:
            print("Turma jovem")
        elif media > 25 and media <= 60:
            print("Turma adulta")
        else:
            print("Turma idosa")
        return

    def exer_26(self):
        # Exercício 26
        # Numa eleição existem três candidatos. Faça um programa que peça o número total de
        # eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada
        # candidato.
        candidatos = {"A": 0, "B": 0, "C": 0}
        for _ in range(int(input("Digite o número de eleitores: "))):
            voto = input(
                f"Digite o voto: ({'/'.join(candidatos.keys())}) ").upper()
            while voto not in candidatos:
                print("Voto inválido")
                voto = input(
                    f"Digite o voto: ({'/'.join(candidatos.keys())}) ").upper()
            candidatos[voto] += 1
        for k, v in candidatos.items():
            print(f"Votos do candidato {k}: {v}")
        return

    def exer_27(self):
        # Exercício 27
        # Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a
        # quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter
        # mais de 40 alunos.
        alunos_por_turma = []
        for i in range(int(input("Digite a quantidade de turmas: "))):
            alunos = int(
                input(f"Digite a quantidade de alunos da {i + 1}º turma: "))
            while alunos > 40:
                print("Turma com mais de 40 alunos")
                alunos = int(
                    input(f"Digite a quantidade de alunos da {i + 1}º turma: "))

            alunos_por_turma.append(alunos)
        print(
            f"Número médio de alunos por turma:{sum(alunos_por_turma) / len(alunos_por_turma)}")
        return

    def exer_28(self):
        # Exercício 28
        # Faça um programa que calcule o valor total investido por um colecionador em sua
        # coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a
        # quantidade de CDs e o valor para em cada um.
        valores = [int(input(f"Digite o valor do {i + 1}º CD: "))
                   for i in range(int(input("Digite a quantidade de CDs: ")))]
        print(f"Valor total investido: {sum(valores)}")
        print(f"Valor médio gasto em cada CD: {sum(valores) / len(valores)}")
        return

    def exer_29(self):
        # Exercício 29
        # O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10
        # caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela
        # que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma
        # a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na
        # tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de
        # preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
        # Lojas Quase Dois - Tabela de preços
        # 1 - R$ 1.99
        # 2 - R$ 3.98
        # ...
        # 50 - R$ 99.50
        for i in range(1, 51):
            print(f"{i} - R$ {i * 1.99}")
        return

    def exer_30(self):
        # Exercício 30
        # O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
        # metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para
        # desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do
        # preço do pão informado pelo usuário, conforme o exemplo abaixo:
        # Preço do pão: R$ 0.18
        # Panificadora Pão de Ontem - Tabela de preços
        # 1 - R$ 0.18
        # 2 - R$ 0.36
        # ...
        # 50 - R$ 9.00
        preco = float(input("Digite o preço do pão: "))
        for i in range(1, 51):
            print(f"{i} - R$ {i * preco}")
        return

    def exer_31(self):
        # Exercício 31
        # O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora
        # possui uma loja de conveniências. Faça um programa que implemente uma caixa
        # registradora rudimentar. O programa deverá receber um número desconhecido de valores
        # referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para
        # indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o
        # valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
        # Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima
        # compra. A saída deve ser conforme o exemplo abaixo:
        # Lojas Tabajara
        # Produto 1: R$ 2.20
        # Produto 2: R$ 5.80
        # Produto 3: R$ 0
        # Total: R$ 9.00
        # Dinheiro: R$ 20.00
        # Troco: R$ 11.00
        while True:
            print("Lojas Tabajara")
            total = 0
            i = 1
            while True:
                produto = float(input(f"Produto {i}: "))
                i += 1
                if produto == 0:
                    break
                total += produto
            print(f"Total: R$ {total}")
            dinheiro = float(input("Dinheiro: R$ "))
            print(f"Troco: R$ {dinheiro - total}")
            if input("Deseja continuar? (S/N) ").upper() == "N":
                break
        return

    def exer_32(self):
        # Exercício 32
        # Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
        # Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
        # Fatorial de: 5
        # 5! = 5 . 4 . 3 . 2 . 1 = 120
        self.exer_17()
        return

    def exer_33(self):
        # Exercício 33
        # O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa
        # que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a
        # maior temperaturas informadas, bem como a média das temperaturas.
        temperaturas = [
            int(input("Digite temperaturas separadas por um espaço:")).split()]
        print(f"Menor temperatura: {min(temperaturas)}")
        print(f"Maior temperatura: {max(temperaturas)}")
        print(
            f"Média das temperaturas: {sum(temperaturas) / len(temperaturas)}")
        return

    def exer_34(self):
        # Exercício 34
        # Os números primos possuem várias aplicações dentro da Computação, por exemplo na
        # Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
        # Faça um programa que peça um número inteiro e determine se ele é ou não um número
        # primo.
        self.exer_21()
        return

    def exer_35(self):
        # Exercício 35
        # Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista
        # dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
        numero = int(input("Digite um número: "))
        primos = [x for x in range(1, numero + 1) if self.primo(x)]
        print(f"Os números primos entre 1 e {numero} são: \n{primos}")
        return

    def exer_36(self):
        # Exercício 36
        numero = int(input("Digite um número: "))
        while numero < 1 or numero > 10:
            print("Número inválido, digite um número entre 1 e 10")
            numero = int(input("Digite um número: "))
        valor_inicial = int(input("Digite um valor inicial: "))
        valor_final = int(input("Digite um valor final: "))
        while valor_final < valor_inicial:
            print("Valor final menor que valor inicial")
            valor_final = int(input("Digite um valor final: "))
        print(f"Tabuada de {numero}")
        for i in range(valor_final, valor_final + 1):
            print(numero, " X ", i, " = ", numero * i)
        return

    def exer_37(self):
        # Exercício 37
        # Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o
        # mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que
        # pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da
        # digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao
        # encerrar o programa também deve ser informados os códigos e valores do clente mais alto,
        # do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos
        # clientes
        clientes = {}
        while True:
            codigo = int(input("Digite o código do cliente: "))
            if codigo == 0:
                break
            altura = float(input("Digite a altura do cliente: "))
            peso = float(input("Digite o peso do cliente: "))
            clientes[codigo] = [altura, peso]
        print(
            f"Cliente mais alto: {max(clientes, key=lambda x: clientes[x][0])}")
        print(
            f"Cliente mais baixo: {min(clientes, key=lambda x: clientes[x][0])}")
        print(
            f"Cliente mais gordo: {max(clientes, key=lambda x: clientes[x][1])}")
        print(
            f"Cliente mais magro: {min(clientes, key=lambda x: clientes[x][1])}")
        print(
            f"Média das alturas: {sum([clientes[x][0] for x in clientes]) / len(clientes)}")
        print(
            f"Média dos pesos: {sum([clientes[x][1] for x in clientes]) / len(clientes)}")
        return

    def exer_38(self):
        # Exercício 38
        # Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
        # a. Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
        # b. Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
        # c. A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do
        # percentual do ano anterior. Faça um programa que determine o salário atual desse
        # funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o
        # salário inicial do funcionário.
        salario_atual = int(input("Digite o salário inicial: "))
        salario_atual += (salario_atual * 0.015)
        percentual_anterior = 0.015
        ano_atual = int(input("Digite o ano atual: "))
        while ano_atual < 1997:
            print("Ano inválido")
            ano_atual = int(input("Digite o ano atual: "))
        for _ in range(1997, ano_atual + 1):
            salario_atual += (salario_atual * percentual_anterior * 2)
            percentual_anterior *= 2
        print("Salário atual: {:.2f}".format(salario_atual))
        return

    def exer_39(self):
        # Exercício 39
        # Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o
        # número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno
        # mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais
        # baixo, junto com suas alturas.
        alunos = {}
        for _ in range(10):
            numero = int(input("Digite o número do aluno: "))
            altura = float(input("Digite a altura do aluno: "))
            alunos[numero] = altura

        print(f"Aluno mais alto: {max(alunos, key=lambda x: alunos[x])}")
        print(f"Aluno mais baixo: {min(alunos, key=lambda x: alunos[x])}")
        return

    def exer_40(self):
        # Exercício 40
        # Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes
        # de trânsito. Foram obtidos os seguintes dados:
        # a. Código da cidade;
        # b. Número de veículos de passeio (em 1999);
        # c. Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
        # d. Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
        # e. Qual a média de veículos nas cinco cidades juntas;
        # f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de
        # passeio.
        cidades = {}
        for _ in range(5):
            codigo = int(input("Digite o código da cidade: "))
            veiculos = int(input("Digite o número de veículos: "))
            acidentes = int(input("Digite o número de acidentes: "))
            cidades[codigo] = [veiculos, acidentes]
        maior_indice = max(cidades[x][1] for x in cidades)
        print(f"Maior índice de acidentes: {maior_indice}")
        print(
            f"Cidade com maior índice de acidentes: {[cidade for cidade in cidades if cidades[cidade][1] == maior_indice][0]}")
        menor_indice = min(cidades[x][1] for x in cidades)
        print(f"Menor índice de acidentes: {menor_indice}")
        print(
            f"Cidade com menor índice de acidentes: {[cidade for cidade in cidades if cidades[cidade][1] == menor_indice][0]}")
        print(
            f"Média de veículos: {sum(cidades[x][0] for x in cidades) / len(cidades)}")
        print(
            f"Média de acidentes: {sum(cidades[x][1] for x in cidades if cidades[x][0] < 2000) / len([x for x in cidades if cidades[x][0] < 2000])}")
        return

    def exer_41(self):
        # Exercício 41
        # Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
        # seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
        # Os juros e a quantidade de parcelas seguem a tabela abaixo:
        # Quantidade de Parcelas % de Juros sobre o valor inicial da dívida
        # 1 0
        # 3 10
        # 6 15
        # 9 20
        # 12 25
        # Exemplo de saída do programa:
        # Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
        # R$ 1.000,00 0 1 R$ 1.000,00
        # R$ 1.100,00 100 3 R$ 366,00
        # R$ 1.150,00 150 6 R$ 191,67
        juros = {
            1: 0,
            3: 0.1,
            6: 0.15,
            9: 0.2,
            12: 0.25
        }
        divida = float(input("Digite o valor da dívida: "))
        print("Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela")
        print(f"R$ {divida:.2f} 0 1 R$ {divida:.2f}")
        for parcelas in [3, 6, 9, 12]:
            print("{}, {}, {}, {:.2f}".format(
                divida, juros[parcelas], parcelas, divida * (1 + juros[parcelas]) / parcelas))
        return

    def exer_43(self):
        # Exercício 43
        # Faça um programa que leia uma quantidade indeterminada de números positivos e conte
        # quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada
        # de dados deverá terminar quando for lido um número negativo.
        numeros = []
        numero = int(input("Digite um número: "))
        while numero >= 0:
            numeros.append(numero)
            numero = int(input("Digite um número: "))
        print(f"Intervalo [0-25]: {len([x for x in numeros if 0 <= x <= 25])}")
        print(
            f"Intervalo [26-50]: {len([x for x in numeros if 26 <= x <= 50])}")
        print(
            f"Intervalo [51-75]: {len([x for x in numeros if 51 <= x <= 75])}")
        print(
            f"Intervalo [76-100]: {len([x for x in numeros if 76 <= x <= 100])}")
        return

    def exer_44(self):
        # Exercício 44
        # Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
        # Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
        # Considere que o cliente deve informar quando o pedido deve ser encerrado.
        # O cardápio de uma lanchonete é o seguinte:
        # Especificação Código Preço
        # Cachorro Quente 100 R$ 1,20
        # Bauru Simples 101 R$ 1,30
        # Bauru com ovo 102 R$ 1,50
        # Hambúrguer 103 R$ 1,20
        # Cheeseburguer 104 R$ 1,30
        # Refrigerante 105 R$ 1,00
        print("Especificação Código Preço")
        print("Cachorro Quente 100 R$ 1,20")
        print("Bauru Simples 101 R$ 1,30")
        print("Bauru com ovo 102 R$ 1,50")
        print("Hambúrguer 103 R$ 1,20")
        print("Cheeseburguer 104 R$ 1,30")
        print("Refrigerante 105 R$ 1,00")

        cardapio = {
            100: 1.2,
            101: 1.3,
            102: 1.5,
            103: 1.2,
            104: 1.3,
            105: 1.0
        }
        while True:
            codigo = int(input("Digite o código do produto: "))
            if codigo == 0:
                break
            if codigo in cardapio:
                quantidade = int(input("Digite a quantidade: "))
                total = 0
                total += cardapio[codigo] * quantidade
                print(
                    f"Valor a ser pago: R$ {cardapio[codigo] * quantidade:.2f}")
            else:
                print("Código inválido!")
        print(f"Total: R$ {total:.2f}")
        return

    def exer_45(self):
        # Exercício 45
        # Em uma eleição presidencial existem quatro candidatos. Os votos são informados por
        # meio de código. Os códigos utilizados são:
        # 1 , 2, 3, 4 - Votos para os respectivos candidatos
        # (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
        # 5 - Voto Nulo
        # 6 - Voto em Branco
        # Faça um programa que calcule e mostre:
        # • O total de votos para cada candidato;
        # • O total de votos nulos;
        # • O total de votos em branco;
        # • A percentagem de votos nulos sobre o total de votos;
        # • A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos
        # tem-se o valor zero.
        votos = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        print("1 - José")
        print("2 - João")
        print("3 - Maria")
        print("4 - Pedro")
        print("5 - Voto Nulo")
        print("6 - Voto em Branco")
        while True:
            voto = int(input("Digite o seu voto: "))
            if voto == 0:
                break
            if voto in votos:
                votos[voto] += 1
            else:
                print("Voto inválido!")
        print("Total de votos para cada candidato:")
        for candidato, voto in votos.items():
            print(f"{candidato} - {voto}")
        print(f"Total de votos nulos: {votos[5]}")
        print(f"Total de votos em branco: {votos[6]}")
        print(
            f"Percentagem de votos nulos: {votos[5] / sum(votos.values()) * 100:.2f}%")
        print(
            f"Percentagem de votos em branco: {votos[6] / sum(votos.values()) * 100:.2f}%")
        return

    def exer_46(self):
        # Exercício 46
        # Desenvolver um programa para verificar a nota do aluno em uma prova com 10
        # questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final
        # comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1
        # ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se
        # outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
        # a. Maior e Menor Acerto;
        # b. Total de Alunos que utilizaram o sistema;
        # c. A Média das Notas da Turma.
        # Gabarito da Prova:
        # 01 - A
        # 02 - B
        # 03 - C
        # 04 - D
        # 05 - E
        # 06 - E
        # 07 - D
        # 08 - C
        # 09 - B
        # 10 - A
        # Após concluir isto você poderia incrementar o programa permitindo que o professor
        # digite o gabarito da prova antes dos alunos usarem o programa.
        gabarito = {}

        for i in range(1, 11):
            gabarito[i] = input(f"Digite a resposta da questão {i}: ")

        lacertos = []
        while True:
            acertos = 0
            for questao in range(1, 11):
                resposta = input(f"Resposta da questão {questao}: ")
                if resposta == gabarito[questao]:
                    acertos += 1
            lacertos.append(acertos)
            total_alunos += 1
            continuar = input("Outro aluno vai utilizar o sistema? (s/n): ")
            if continuar == "n":
                break
        print(f"Maior acerto: {max(lacertos)}")
        print(f"Menor acerto: {min(lacertos)}")
        print(f"Total de alunos: {total_alunos}")
        print(f"Média das notas: {sum(lacertos) / total_alunos:.2f}")
        return

    def exer_47(self):
        # Exercício 47
        # Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final
        # da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado
        # fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o
        # nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média
        # dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois
        # calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados
        # na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando
        # não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo
        # abaixo:
        # Atleta: Rodrigo Curvêllo
        # Primeiro Salto: 6.5 m
        # Segundo Salto: 6.1 m
        # Terceiro Salto: 6.2 m
        # Quarto Salto: 5.4 m
        # Quinto Salto: 5.3 m
        # Melhor salto: 6.5 m
        # Pior salto: 5.3 m
        # Média dos demais saltos: 5.9 m
        # Resultado final:
        # Rodrigo Curvêllo: 5.9 m
        while True:
            nome = input("Digite o nome do atleta: ")
            if nome == "":
                break
            saltos = [float(input(f"Digite o {i}º salto: "))
                      for i in range(1, 6)]
            saltos.sort()
            print(f"Atleta: {nome}")
            for i, salto in enumerate(saltos):
                print(f"{i + 1}º Salto: {salto} m")
            print(f"Melhor salto: {saltos[-1]} m")
            print(f"Pior salto: {saltos[0]} m")
            print(
                f"Média dos demais saltos: {sum(saltos[1:-1]) / len(saltos[1:-1]):.1f} m")
            print(
                f"Resultado final: {nome}: {sum(saltos[1:-1]) / len(saltos[1:-1]):.1f} m")
        return

    def exer_48(self):
        # Exercício 48
        # Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a
        # pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer
        # um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo
        # atleta em sua apresentação e depois informe a sua média, conforme a descrição acima
        # informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes).
        # As notas não são informados ordenadas. Um exemplo de saída do programa deve ser
        # conforme o exemplo abaixo:
        # Atleta: Aparecido Parente
        # Nota: 9.9
        # Nota: 7.5
        # Nota: 9.5
        # Nota: 8.5
        # Nota: 9.0
        # Nota: 8.5
        # Nota: 9.7
        # Resultado final:
        # Atleta: Aparecido Parente
        # Melhor nota: 9.9
        # Pior nota: 7.5
        # Média: 9,04
        while True:
            nome = input("Digite o nome do atleta: ")
            if nome == "":
                break
            notas = [float(input(f"Digite a {i}º nota: "))
                     for i in range(1, 8)]
            notas.sort()
            print(f"Atleta: {nome}")
            for nota in notas:
                print(f"Nota: {nota}")
            print(f"Melhor nota: {notas[-1]}")
            print(f"Pior nota: {notas[0]}")
            print(f"Média: {sum(notas[1:-1]) / len(notas[1:-1]):.2f}")
        return

    def exer_49(self):
        # Exercício 49
        # Faça um programa que peça um numero inteiro positivo e em seguida mostre este
        # numero invertido.
        # Exemplo:
        # 12376489
        # => 98467321
        numero = input("Digite um número inteiro positivo: ")
        print("=>", numero[::-1])
        return

    def exer_50(self):
        # Exercício 50
        # Faça um programa que mostre os n termos da Série a seguir:
        # S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
        # Imprima no final a soma da série.
        n = int(input("Digite o valor de n: "))
        soma = sum(i / (2 * i - 1) for i in range(1, n + 1))
        print(f"Soma: {soma:.2f}")
        return

    def exer_51(self):
        # Exercício 51
        # Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H
        # com N termos.
        n = int(input("Digite o valor de n: "))
        soma = sum(1 / i for i in range(1, n + 1))
        print(f"Soma: {soma:.2f}")
        return

    def exer_52(self):
        # Exercício 52
        # Faça um programa que mostre os n termos da Série a seguir:
        # S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
        # Imprima no final a soma da série.
        n = int(input("Digite o valor de n: "))
        for i in range(1, n + 1):
            print(f"{i}/{2 * i - 1}", end=" ")
        print(sum(i / (2 * i - 1) for i in range(1, n + 1)))
        return


if __name__ == '__main__':
    while True:
        Exercises(int(input("Digite o exercício desejado: ")))
        if input("Deseja testar mais exercícios? (s/n) ").lower() == "n":
            print("Fim do programa")
            break
