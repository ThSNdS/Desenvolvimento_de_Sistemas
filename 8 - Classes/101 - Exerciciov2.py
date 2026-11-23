from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    # NOME DA VARIÁVEL : TIPO DA VARIÁVEL
    nome: str
    idade: int

# SOLICITANDOS DADOS DE UM CLIENTE.
cliente1 = Cliente('Marta', 30)

# SOLICITANDOS DADOS DE OUTRO CLIENTE.
cliente2 = Cliente('José', 40)

print(f'Nome: {cliente1.nome}')
print(f'Idade: {cliente1.idade}')

print(f'Nome: {cliente2.nome}')
print(f'Idade: {cliente2.idade}')