from dataclasses import dataclass
import os
os.system('cls')

@dataclass
class Produto:
    nome: str
    preco: float

lista_produtos = []

def absolver_dados():
    for i in range (3):
        produto = Produto
        nome = input('Digite o nome do produto: ')
        preco = float(input('Digite o preço: '))
        lista_produtos.append(produto)

def mostrar_dados(lista_produtos):
    for produto in lista_produtos:
        print(f'{produto.nome} - {produto.preço}')

print('= SOLICITANDO DADOS =')

absolver_dados()

print('\n= EXIBINDO DADOS =')
mostrar_dados(lista_produtos)