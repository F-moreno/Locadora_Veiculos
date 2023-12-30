class Veiculo:
    def __init__(self, modelo, ano, diaria, placa, locado=False) -> None:
        self.modelo = modelo
        self.ano = ano
        self.diaria = diaria
        self.placa = placa
        self.locado = locado

    def alugar(self):
        try:
            if not self.locado:
                self.locado = True
            else:
                raise Exception(f"{self.modelo} já alugado!")
        except Exception as e:
            print(f"Erro: {e}")

    def devolver(self):
        try:
            if self.locado:
                self.locado = False
            else:
                raise Exception(
                    f"Não é possível devolver o {self.modelo}, pois ainda não está alugado!"
                )
        except Exception as e:
            print(f"Erro: {e}")


class Portfolio:
    def __init__(self, veiculos=[]) -> None:
        self.veiculos = veiculos
        self.index = 0

    def addveiculo(self, carro):
        self.veiculos.append(carro)

    def rmveiculo(self, carro):
        try:
            self.veiculos.remove(carro)
        except ValueError:
            print(f"Error: {carro} not found in veiculos list.")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.veiculos):
            retorno = self.veiculos[
                self.index
            ]  # pega o item no index 0 / index 1 / ...
            self.index += 1  # altera o valor do index para index+1 / (index+1)+1 / ...
            return retorno  # retorna o veiculo na posição retorno
        else:
            self.index = 0  # reinicializa o index para poder fazer iterações futuras
            raise StopIteration  # sobe a excessão de parada.

    def __str__(self):
        return "Objeto Portfolio"


# # # teste

# carro = Veiculo("Geek", 2016, 50, 1)
# carro2 = Veiculo("Corza", 2008, 40, 2)


# # print(carro.locado)
# # carro.devolver()  # faz com que o status do carro seja alterado para true
# # print(carro.locado)
# # carro.alugar()  # faz com que o status do carro seja alterado para true
# # print(carro.locado)'

# p = Portfolio()

# p.addveiculo(carro)
# p.addveiculo(carro2)

# for c in p:
#     print(c.modelo)

# p.rmveiculo(carro)

# for c in p:
#     print(c.modelo)

"""
JHU7A6:{
    MODELO: XXXX
    MARCA: YYYY
}
"""
