# Questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro = Carro("Bmw", "Vermelha", 2000)
print(f"Modelo: {carro.modelo}, Cor: {carro.cor}, Ano: {carro.ano}")

# Questões 2, 3 e 4
class Restaurante:
    def __init__(self, nome, categoria, endereco, capacidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = endereco
        self.capacidade = capacidade

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}, Ativo: {self.ativo}, Endereço: {self.endereco}, Capacidade: {self.capacidade}"

restaurante = Restaurante("Pasta House", "Italiana", "Rua dos Pinhais, 789", 120)
print(restaurante)

# Questão 5
class Cliente:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

# Instanciando 3 objetos da classe Cliente e atribuindo valores aos seus atributos
cliente1 = Cliente('Eduarda Mouro', 'dudaMouro@hotmail.com', '1934-2671', 'Rua A, 117')
cliente2 = Cliente('Pedro Brecher', 'pedroBrecher@hotmail.com', '9761-4251', 'Rua B, 280')
cliente3 = Cliente('Ana Luia', 'anaLuiza@hotmail.com', '1572-3974', 'Rua C, 390')

print(f"Cliente 1: Nome: {cliente1.nome}, Idade: {cliente1.idade}, CPF: {cliente1.cpf}, Email: {cliente1.email}")
print(f"Cliente 2: Nome: {cliente2.nome}, Idade: {cliente2.idade}, CPF: {cliente2.cpf}, Email: {cliente2.email}")
print(f"Cliente 3: Nome: {cliente3.nome}, Idade: {cliente3.idade}, CPF: {cliente3.cpf}, Email: {cliente3.email}")
