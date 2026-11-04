import os

lista_nomes = []
lista_posicoes = []
lista_camisas = []
while True:
    os.system('cls')
    print('''
=== GERENCIAMENTO DO ELENCO ===
1. Cadastar jogador
2. Listar jogador
3. Atualizar jogador
4. Excluir jogador
0. Sair
''')
    opcao = int(input('Escolha uma opção: '))
    match opcao:
        case 1:
            print('### CADASTRANDO JOGADOR ###')
            nome = input('Digite o nome do jogador: ').upper()
            posicao = input(f'Digite a posição de {nome}: ').upper()
            camisa = int(input(f'Digite a camisa de {nome}: '))
            if nome in lista_nomes or camisa in lista_camisas:
                print('Jogador já foi cadastrado ou camisa já registrada.')
            elif nome == "" or posicao == "" or camisa <= 0:
                print('todos os campos precisam ser prenchidos.')
            else:
                lista_nomes.append(nome)
                lista_posicoes.append(posicao)
                lista_camisas.append(camisa)
            input('Pressione uma tecla para continuar...')
        case 2:
            if len(lista_nomes) == 0:
                print('Nenhuma jogador registrado.')
            else:
                for i in range(len(lista_nomes)):
                    print(f'{i+1}ºjogador | {lista_nomes[i]} | {lista_posicoes[i]} | {lista_camisas[i]}')
                input('Pressione uma tecla para continuar...')
        case 3:
            print('### ATUALIZANDO DADOS DOS JOGADORES ###')
            lugar = int(input('Digite que o número do jogador que deseja atualizar, 1º, 2º ou... : '))
            indice = lugar - 1
            if indice < 0 or indice >= len(lista_nomes):
                print('Jogador não encontrado.')
            else:
                print(lista_nomes[indice])
                tipo = input('Deseja atualizar o nome, posição ou camisa? ').upper()
                match tipo:
                    case 'NOME':
                        novo_nome = input('Digite o novo nome: ').upper()
                        lista_nomes[indice] = novo_nome
                    case 'POSIÇÃO':
                        nova_posicao = input('Digite a nova posiçao: ').upper()
                        lista_posicoes[indice] = nova_posicao
                    case 'CAMISA':
                        nova_camisa = int(input('Digite o novo número da camisa: '))
                        lista_camisas[indice] = nova_camisa
                    case _:
                        print('Opção inválida.')
            input('Pressione uma tecla para continuar...')
        case 4:
            print('== REMOVER JOGADOR ==')
            nome = input('Qual jogador deseja remover? ').upper()
            if nome in lista_nomes:
                lista_nomes.remove(nome)
                print('Jogador alterado com sucesso!')
            else:
                print('Jogador não encontrado.')
            input('Pressione uma tecla para continuar...')
        case 0:
            print('Tem certeza que deseja sair?')
            resposta = input('Digite S pra sim ou qualquer outra tecla pra não: ').upper()
            if resposta == 'S':
                break
        case _:
            input('Pressione uma tecla para continuar...')
