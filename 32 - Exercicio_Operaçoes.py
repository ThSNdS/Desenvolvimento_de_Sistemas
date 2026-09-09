import os
os.system("cls")

print('Atenção: + = Soma, - = Subtração, * = Multplicação e / = Divisão.')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
opera = input('Escolha o tipo de operação de desejada com base nos símbolos: ')

match opera:
    case '+':
        resual = num1 + num2
    case '-':
        resual = num1 - num2
    case '*':
        resual = num1 * num2
    case '/':
        resual = num1 / num2
    case _:
        print('Operação inválida')

print(f'O resultado é:{resual}')