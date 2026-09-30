import os
os.system("cls")

orde = str(input('Deseja ver o cardápio ou efetuar uma pedido?\n Escrevar | menu | para ver o cardápio.\nEscreva | compra | para fazer um pedido: '))


if orde == 'menu':
    print('Código | Prato | Valor \n 1 | Picanha | 25.00 \n 2 | Lasanha | 20.00 \n 3 | Strogonoff | 18.00 \n 4 | Bife Acebolado | 15.00 \n 5 | Pão com ovo | 5.00')
elif orde == 'compra':
    codig = int(input('Digite o código do prato: '))
    match codig:
        case 1:
            print('Picanha: 25.00')
        case 2:
            print('Lasanha: 20.00')
        case 3:
            print('Strogonoff: 18.00')
        case 4:
            print('Bife Acebolado: 15.00')
        case 5:
            print('Pão com Ovo: 5.00')
        case _:
            print('Código inválido')