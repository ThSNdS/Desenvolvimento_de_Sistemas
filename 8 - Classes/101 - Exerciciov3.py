from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    # NOME DA VARIÁVEL : TIPO DA VARIÁVEL
    nome: str
    idade: int

lista_cliente = []

# SOLICITANDOS DADOS DE DOIS CLIENTES.
lista_cliente.append(Cliente(nome='Marta', idade=30))
lista_cliente.append(Cliente('José', 40))

for cliente in lista_cliente:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'='*15)