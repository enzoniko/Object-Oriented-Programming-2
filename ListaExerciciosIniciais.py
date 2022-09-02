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
        print(
            list(
                range(
                    int(input("Digite o primeiro número: ")),
                    int(input("Digite o segundo número: ")) + 1,
                )
            )
        )

        return

    def exer_11(self):
        # Exercício 11
        # Altere o programa anterior para mostrar no final a soma dos números.
        print(
            sum(
                list(
                    range(
                        int(input("Digite o primeiro número: ")),
                        int(input("Digite o segundo número: ")) + 1,
                    )
                )
            )
        )

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


if __name__ == '__main__':
    while True:
        Exercises(int(input("Digite o exercício desejado: ")))
        if input("Deseja testar mais exercícios? (s/n) ").lower() == "n":
            print("Fim do programa")
            break
