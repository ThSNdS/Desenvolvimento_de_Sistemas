import os

lista_nomes = []
lista_sobrenomes = []

while True:
    os.system('cls')
    print('''
=== GERENCIAMENTO DO HOSPITAL ===
1. Cadastar paciente
2. Listar paciente
3. Atualizar paciente
4. Excluir paciente
0. Sair
''')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('### CADASTRANDO PACIENTE ###')
            nome = input('Digite o nome do PACIENTE: ').lower()
            sobrenome = input(f'Digite o sobrenome de {nome}: ').lower()
            if nome in lista_nomes :
                print('Paciente já foi cadastrado.')
            elif nome == "" or sobrenome == "":
                print('todos os campos precisam ser prenchidos.')
            else:
                lista_nomes.append(nome)
                lista_sobrenomes.append(sobrenome)
            input('Pressione uma tecla para continuar...')
        case 2:
            if len(lista_nomes) == 0:
                print('Nenhuma paciente registrado.')
            else:
                for i in range(len(lista_nomes)):
                    print(f'{i+1}ºpaciente | {lista_nomes[i]} | {lista_sobrenomes[i]}')
                input('Pressione uma tecla para continuar...')
        case 3:
            print('### ATUALIZANDO DADOS DOS PACIENTES ###')
            lugar = int(input('Digite que o número do paciente que deseja atualizar, 1º, 2º ou... : '))
            indice = lugar - 1
            if indice < 0 or indice >= len(lista_nomes):
                print('Paciente não encontrado.')
            else:
                print(lista_nomes[indice])
                tipo = input('Deseja atualizar o nome ou sobrenome? ').lower()
                match tipo:
                    case 'nome':
                        novo_nome = input('Digite o novo nome: ').lower()
                        lista_nomes[indice] = novo_nome
                    case 'sobrenome':
                        nova_sobrenome = input('Digite o novo sobrenome: ').lower()
                        lista_sobrenomes[indice] = nova_sobrenome
                    case _:
                        print('Opção inválida.')
            input('Pressione uma tecla para continuar...')
        case 4:
            print('== REMOVER PACIENTE ==')
            nome = input('Qual paciente deseja remover? ').lower()
            if nome in lista_nomes:
                lista_nomes.remove(nome)
                print('Paciente alterado com sucesso!')
            else:
                print('Paciente não encontrado.')
            input('Pressione uma tecla para continuar...')
        case 0:
            print('Tem certeza que deseja sair?')
            resposta = input('Digite S pra sim ou qualquer outra tecla pra não: ').lower()
            if resposta == 's':
                break
        case _:
            input('Pressione uma tecla para continuar...')