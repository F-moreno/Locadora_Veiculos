from modulos import funcoes as f

ano = input("Entre o ano do veiculo: ")
modelo = input("Entre o modelo do veiculo: ")
valor = input("Entre o valor da diaria do veiculo: ")


carro = f.criar_veiculos(ano, modelo, valor)
carro = f.criar_veiculos()
f.criar_veiculos()
