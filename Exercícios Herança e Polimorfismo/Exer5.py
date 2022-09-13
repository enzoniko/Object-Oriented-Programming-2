class Forma():
    def __init__(self, *args, **kwargs):
        if "tipo" in kwargs:
            self.tipo = kwargs["tipo"]
        if "lados" in kwargs:
            self.lados = kwargs["lados"]
        if "raio" in kwargs:
            self.raio = kwargs["raio"]

    def area(self):
        if self.tipo:
            if self.tipo == "quadrado" and self.lados:
                return self.lados[0] ** 2
            elif self.tipo == "retangulo" and self.lados:
                return self.lados[0] * self.lados[1]
            elif self.tipo == "circulo" and self.raio:
                return 3.14 * self.raio ** 2

    def perimetro(self):
        if self.tipo:
            if self.tipo == "quadrado" or self.tipo == "retangulo" and self.lados:
                return sum(self.lados)
            elif self.tipo == "circulo" and self.raio:
                return 2 * 3.14 * self.raio

    def imprime(self):
        print(f"Tipo: {self.tipo}")
        if self.tipo in ["quadrado", "retangulo"]:
            print(f"Lados: {self.lados}")
        elif self.tipo == "circulo":
            print(f"Raio: {self.raio}")
        print(f"Área: {self.area()}")
        print(f"Perímetro: {self.perimetro()}")


class Quadrilateros(Forma):
    def __init__(self, tipo, lado1, lado2, lado3, lado4):
        super().__init__(tipo=tipo, lados=[lado1, lado2, lado3, lado4])
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4
        self.tipo = tipo


class Retangulo(Quadrilateros):
    def __init__(self, base, altura):
        super().__init__("retangulo", base, altura, base, altura)


class Quadrado(Quadrilateros):
    def __init__(self, lado):
        super().__init__("quadrado", lado, lado, lado, lado)


class Circulo(Forma):
    def __init__(self, raio):
        super().__init__(tipo="circulo", raio=raio)
        self.raio = raio


def main():
    formas = []
    quantidade_formas = int(input("Digite a quantidade de formas: "))
    for _ in range(quantidade_formas):
        tipo_forma = input(
            "Digite o tipo de forma: (1:quadrado, 2:retangulo, 3:circulo)")
        if tipo_forma == "1":
            lado = int(input("Digite o lado: "))
            forma = Quadrado(lado)

        if tipo_forma == "2":
            base = int(input("Digite a base: "))
            altura = int(input("Digite a altura: "))
            forma = Retangulo(base, altura)

        if tipo_forma == "3":
            raio = int(input("Digite o raio: "))
            forma = Circulo(raio)

        forma.imprime()
        formas.append(forma)
    return


if __name__ == "__main__":
    main()
