from modulos.classes import *

"""
seu sistema deve permitir que o usuario crie, e exclua veículos e portifolios.
o sistema deve permitir listar os veiculos do portifolio, alugar e selecionar veiculos para alugar
"""


def criar_veiculos() -> Veiculo:
    _ano = input("digite o ano do veiculo: ")
    _modelo = input("digite o modelo do veiculo: ")
    _diaria = input("digite o preço da diária do veiculo: ")
    _placa = input("digite a placa do veiculo: ")

    _carro = Veiculo(_ano, _modelo, _diaria, _placa)
    return _carro


def deletar_veiculo(portfolio: Portfolio, carro) -> Portfolio:
    _portfolio = portfolio.rmveiculo(carro)
    return _portfolio


def criar_portfolio() -> Portfolio:
    pass


def deletar_portfolio():
    pass


"""
portfolios:

disponíveis = []
alugados = []

"""
