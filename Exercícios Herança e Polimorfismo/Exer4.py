from Exer1 import *
from Exer2 import *
from Exer3 import *


class Teste():
    def __init__(self):
        return

    def main(self):
        Assistente_Tecnico("João", 1000, 123, "Informática").exibeDados()
        Assistente_Administrativo("Maria", 1000, 456, "noturno").exibeDados()
        tipo_ingresso = input("Digite o tipo de ingresso: (1:normal, 2:vip)")
        if tipo_ingresso == "1":
            Normal(100).imprimeIngressoNormal()
        if tipo_ingresso == "2":
            tipo_camarote = input(
                "Digite o tipo de camarote: (1:inferior, 2:superior)")
            if tipo_camarote == "1":
                CamaroteInferior(100, 50, "A").imprimeLocal()
            else:
                CamaroteSuperior(100, 50, "B", 50).imprimeValor()
        tipo_imovel = input("Digite o tipo de imóvel: (1:velho, 2:novo)")
        if tipo_imovel == "1":
            Velho('A', 300000, 0.25).imprimeValor()
        if tipo_imovel == "2":
            Novo('B', 500000, 50000).imprimeValor()


# Inheritance overloading parameters error???
Teste().main()
