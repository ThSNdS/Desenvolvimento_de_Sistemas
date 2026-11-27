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

arquivo = 'dados_fornecedores.csv'
with open(arquivo, 'r') as arquivo_fornecedores:
    for linha in arquivo_fornecedores:
        nome, e_mail, telefone, endereco = linha.strip().split(',')
        lista_fornecedores.append(Fornecedores(
            nome=nome,
            e_mail=e_mail,
            telefone=telefone,
            endereco=endereco
        ))

print('\nExibindo dados dos fornecedores: ')
for fornecedor in lista_fornecedores:
    print(f'Nome: {fornecedor.nome}')
    print(f'E-mail: {fornecedor.e_mail}')
    print(f'Telefone: {fornecedor.telefone}')
    print(f'Endereço: {fornecedor.endereco}')
    print('='*25)