import os
os.system('cls')

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
                def cadastar_cliente(nome, email, telefone):
                    nome = input('Digite seu nome: ')
                    email = input('Digite seu email: ')
                    telefone = input('Digite seu telefone: ')
                    print("= Cadastrando Cliente =")
                    cadastar_cliente(nome, email, telefone)
            case '2':
                def mostrar_dados(nome, email, telefone):
                    print(f'O email {email} e número {telefone} são de {nome}')
                    mostrar_dados(nome, email, telefone)
            case '3':
                def exit():
                    print('Fechando Programa.')
                    exit()
            case _:
                print('Opção inválida.')