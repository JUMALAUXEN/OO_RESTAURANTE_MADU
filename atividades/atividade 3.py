# Questão 1
class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    @property
    def saudacao(self):
        return f"Oi, meu nome é {self.nome} e eu sou {self.profissao}."

pessoa = Pessoa("Gabriela Moraes", 26, "Médica")
print(pessoa)
pessoa.aniversario()
print(pessoa)
print(pessoa.saudacao)

# Questões 2, 3, 4 e 5
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f"Titular: {self.titular}, Saldo: R${self.saldo:.2f}"

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

conta1 = ContaBancaria("Rafael Rofman", 3500)
conta2 = ContaBancaria("Beatriz Almada", 4700)
print(conta1)
print(conta2)

conta = ContaBancaria("Paula Costa", 2000)
ContaBancaria.ativar_conta(conta)
print(conta.ativo)

# Questão 6
conta = ContaBancaria("Mariana Mouro", 7500)
print(conta.titular)

# Questões 7 e 8
class ClienteBanco:
    def __init__(self, nome, idade, endereco, telefone, email):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    @classmethod
    def criar_conta(cls, cliente, saldo_inicial):
        return ContaBancaria(cliente.nome, saldo_inicial)

cliente1 = ClienteBanco("Lucas Ferreira", 50, "Av. Paulista, 740", "31987654321", "lucasAndrade@hotmail.com")
cliente2 = ClienteBanco("Amanda Rocha", 35, "Rua das Flores, 601", "41987654321", "amandaRocha@hotmail.com")
cliente3 = ClienteBanco("Fernanda Andrade", 29, "Praça da Sé, 389", "11987654321", "fernandaAndrade@hotmail.com")

cliente = ClienteBanco("Maria Costa", 29, "Praça da Fé, 520", "21987654321", "mariaCosta")
conta = ClienteBanco.criar_conta(cliente, 3000)
print(conta)
