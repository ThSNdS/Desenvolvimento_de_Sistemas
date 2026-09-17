import os
os.system('cls')

cor = input('Digite a cor do CD: ').lower()

match cor:
    case 'verde':
        print('CD Verde por R$: 10,00 ')
    case 'azul':
        print('CD Azul por R$: 20,00 ')
    case 'amarelo':
        print('CD Amarelo por R$: 30,00 ')
    case 'vermelho':
        print('CD Vermelho por R$: 40,00 ')
    case _:
        print('Cor inválida.')
