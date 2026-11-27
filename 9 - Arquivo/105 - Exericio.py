from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Fornecedores:
    nome: str
    e_mail: str
    telefone: int
    endereco: int

QUANTIDADES_DE_FORNECEDORES = 3

lista_fornecedores = []

for i in range(QUANTIDADES_DE_FORNECEDORES):
    novo_fornecedor = Fornecedores(
        nome= input('Digite seu nome: '),
        e_mail= input('Digite seu e-mail: '),
        telefone= int(input('Digite seu telefone: ')),
        endereco= int(input('Digite seu endereço: '))
    )
    lista_fornecedores.append(novo_fornecedor)

arquivo = 'dados_fornecedores.csv'
with open(arquivo, 'a') as arquivo_de_fornecedores:
    for fornecedor in lista_fornecedores:
        arquivo_de_fornecedores.write(f'{fornecedor.nome}, {fornecedor.e_mail}, {fornecedor.telefone}, {fornecedor.endereco}\n')

print('Fornecedores salvos com sucesso!')