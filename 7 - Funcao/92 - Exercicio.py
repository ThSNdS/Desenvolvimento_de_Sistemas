import os
os.system('cls')

def calculo():
    print(f'\nA tabuada de {numero} é')
    for i in range(1,11):
        print(f'{i}º {numero * i}')

numero = int(input('Digite um número: '))

calculo()

