import os
os.system('cls')
nome = ''
email = ''
telefone = ''

def cadastar_cliente(nome, email, telefone):
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    telefone = input('Digite seu telefone: ')
def mostrar_dados(nome, email, telefone):
    print(f'O email {email} e número {telefone} são de {nome}')
def exit():
    print('Fechando Programa.')
    

while True:
        print('''
    === SHOPPING BAHIA ===
    1. CADASTAR CLIENTE
    2. MOSTRAR DADOS DO CLIENTE
    3. Sair
    ''')
        opcao = input('Escolha uma opção: ')
        match opcao:
            case '1':
                    print("= Cadastrando Cliente =")
                    cadastar_cliente(nome, email, telefone)
            case '2':
                    mostrar_dados(nome, email, telefone)
            case '3':
                    exit()
                    break
            case _:
                print('Opção inválida.')