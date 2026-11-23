from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Cliente:
    # NOME DA VARIÁVEL : TIPO DA VARIÁVEL
    nome: str
    idade: int
    altura: float
    peso: float

lista_cliente = []

# SOLICITANDOS DADOS DE DOIS CLIENTES.
for i in range(2):
    dados_do_cliente = Cliente(
        nome= input('Digite o nome do cliente: '),
        idade= int(input('Digite sua idade: ')),
        altura= float(input('Digite sua altura: ')),
        peso= float(input('Digite seu peso: '))
        )
    lista_cliente.append(dados_do_cliente)

for cliente in lista_cliente:
    print(f'Nome: {cliente.nome}')
    print(f'Idade: {cliente.idade}')
    print(f'Altura: {cliente.altura}')
    print(f'Peso: {cliente.peso}')
    print(f'='*15)