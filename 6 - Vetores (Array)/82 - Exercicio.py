import os
os.system('cls')

vetor_valor = []
valor = 0
vetor_pratos = []
codigos = 0

print('''
Menu
Código|     Prato      | Valor
   1  | Picanha        | 25,00
   2  | Lasanha        | 20,00
   3  | Strogonoff     | 18,00
   4  | Bife Acebolado | 15,00
   5  | Pão com Ovo    |  5,00
''')
while True:
    codigo = input('Digite o Código do escolhido: ')
    match codigo:
        case '1':
            valor += 25.00
            vetor_pratos.append('Picanha')
            vetor_valor.append(25.00)
            codigos += 1
        case '2':
            valor += 20.00
            vetor_pratos.append('Lasanha')
            vetor_valor.append(20.00)
            codigos += 1
        case '3':
            valor += 18.00
            vetor_pratos.append('Strogonoff')
            vetor_valor.append(18.00)
            codigos += 1
        case '4':
            valor += 15.00
            vetor_pratos.append('Bife Acebolado')
            vetor_valor.append(15.00)
            codigos += 1
        case '5':
            valor += 5.00
            vetor_pratos.append('Pão com Ovo')
            vetor_valor.append(5.00)
            codigos += 1
        case _:
            print('Código Inválido.')
    resposta = input('Dejesa pedir outro prato (S/N): ').upper()
    if resposta == 'N':
        break


if codigos <= 0:
    print('Nenhum pedido realizado.')
else:
    print(f'Prato: {vetor_pratos}')
    print(f'valor: {vetor_valor}')
    print(f'\nValor total: {valor}')
