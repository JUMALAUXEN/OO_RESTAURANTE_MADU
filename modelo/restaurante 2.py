# 1 criando uma classe usando construtor

class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        
        def __STR__(self):
            #return self.nome
            return f'{self.nome}' | {self.categoria} | {self.ativo}

restaurante_praca = Restaurante()
restaurante_praca = Restaurante ('Praça', 'Gourmet')
restaurante_praca.categoria='Italiana'
restaurante_praca.ativo="ativo" if restaurante_praca.ativo else "inativo"

print(f"O restaurante está {restaurante_praca}.")

print(f"Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}")

restaurante_pizza=Restaurante()
restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
restaurante_pizza.ativo=True

restaurantes=[restaurante_praca,restaurante_pizza]

print(dir(restaurante_praca))
print('')
print(vars(restaurante_praca))
print('')
print(restaurante_praca)