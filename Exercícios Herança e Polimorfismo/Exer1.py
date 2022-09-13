class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def setNome(self, nome):
        self.nome = nome

    def setSalario(self, salario):
        self.salario = salario

    def exibeDados(self):
        print("Nome: ", self.nome)
        print("Salário: ", self.salario)


class Gerente(Funcionario):
    def __init__(self, nome, salario, senha, numFuncionarios):
        super().__init__(nome, salario)
        self.senha = senha
        self.numFuncionarios = numFuncionarios

    def getSenha(self):
        return self.senha

    def getNumFuncionarios(self):
        return self.numFuncionarios

    def setSenha(self, senha):
        self.senha = senha

    def setNumFuncionarios(self, numFuncionarios):
        self.numFuncionarios = numFuncionarios

    def autentica(self, senha):
        if self.senha == senha:
            print("Acesso permitido")
        else:
            print("Acesso negado")

    def exibeDados(self):
        super().exibeDados()
        print("Senha: ", self.senha)
        print("Número de funcionários: ", self.numFuncionarios)


class Assistente(Funcionario):
    def __init__(self, nome, salario, matricula):
        super().__init__(nome, salario)
        self.matricula = matricula

    def getMatricula(self):
        return self.matricula

    def setMatricula(self, matricula):
        self.matricula = matricula

    def exibeDados(self):
        super().exibeDados()
        print("Matrícula: ", self.matricula)


class Assistente_Tecnico(Assistente):
    def __init__(self, nome, salario, matricula, especialidade):
        super().__init__(nome, salario, matricula)
        self.especialidade = especialidade
        self.salario = salario + 1000

    def getEspecialidade(self):
        return self.especialidade

    def setEspecialidade(self, especialidade):
        self.especialidade = especialidade

    def exibeDados(self):
        super().exibeDados()
        print("Especialidade: ", self.especialidade)


class Assistente_Administrativo(Assistente):
    def __init__(self, nome, salario, matricula, turno):
        super().__init__(nome, salario, matricula)
        self.turno = turno
        if self.turno == "noturno":
            self.salario = salario + 500

    def getTurno(self):
        return self.turno

    def setTurno(self, turno):
        self.turno = turno

    def exibeDados(self):
        super().exibeDados()
        print("Turno: ", self.turno)
