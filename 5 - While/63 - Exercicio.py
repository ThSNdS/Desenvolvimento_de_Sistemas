import os
import time
os.system('cls')

print('''   Menu
1 = Picanha R$:35
2 = Batata Frita R$:21
3 = Salada R$:7
4 = Torresmo R$:14
5 = Feijoada R$:28
''')
time.sleep(5)
os.system('cls')

while True:
    pedido = int(input('Digite o numero do pedido: '))
    match pedido:
        case 1:
            Alimento = 'Picanha'
            Valor = 35
            break
        case 2:
            Alimento = 'Batata Frita'
            Valor = 21
            break
        case 3:
            Alimento = 'Salada'
            Valor = 7
            break
        case 4:
            Alimento = 'Torresmo'
            Valor = 14
            break
        case 5:
            Alimento = 'Feijoada'
            Valor = 28
            break
        case _:
            print('Número inválido.')

print(f'Você ira pagar R$:{Valor} por Escolher {Alimento}')