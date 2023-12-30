# Sistema de Gerenciamento para Locação de Veículos:
Desenvolva um sistema para a administração de uma concessionária de aluguel de veículos, seguindo as  seguintes especificações:

# Classe Veículo: 
A classe Veículo deve possuir atributos como modelo, ano, valor da diária e estado (alugado ou não). Implemente funcionalidades para a modificação de estados, de modo que, ao ser chamado, o veículo possa ser alugado ou devolvido.

O sistema deve incorporar verificações de exceções para evitar que um veículo já alugado seja alugado novamente, bem como para garantir que não seja possível devolvê-lo caso não esteja alugado. Isso significa que, ao tentar modificar o estado de um veículo, o sistema deve verificar a ação, tratar e gerar uma exceção quando necessário para impedir essa ação inadequada.

# Classe Portfólio: 
A classe Portfólio deve armazenar uma lista de Veículos. Inclua um método iterator (__iter__ e __next__) para percorrer a lista de veículos.

# Funções:

seu sistema deve permitir que o usuario crie, e exclua veículos e portifolios.
o sistema deve permitir listar os veiculos do portifolio, alugar e selecionar veiculos para alugar

listar veiculos nao alugados e permitir aluga-los
listar veiculos alugados e permitir devolve-los

Certifique-se de que o sistema seja claro e eficiente, proporcionando uma administração intuitiva e segura dos veículos no contexto da locação. 