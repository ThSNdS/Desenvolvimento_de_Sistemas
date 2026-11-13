import os
os.system('cls')

# Função sem retorno e sem parametros
def logo_senai():
    os.system('cls')
    print('=========')
    print('  SENAI  ')
    print('=========')

# Função sem retorno e com parametros
def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos')

# Função sem retorno e sem parametros
logo_senai()
print('\n= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

logo_senai()
print('\n= EXIBINDO DADOS =')
# Função sem retorno e com parametros
mostrar_dados(nome, idade)