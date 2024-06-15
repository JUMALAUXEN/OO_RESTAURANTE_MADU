
# 1 criando uma classe em python
class Restaurante:
    nome=''
    categoria=''
    ativo=False

restaurante_praca=Restaurante()

restaurante_praca.nome='Bistrô'


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
