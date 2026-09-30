import os
os.system("cls")

xx = input('Qual é seu sexo: ').upper()
altura = float(input('Escreva sua altura: '))

match xx:
    case 'M':
        formula = (72.7 * altura) - 58
        print(f'\nO seu peso ideal é: {formula:.2f}')
    case 'F':
        formula = (62.1 * altura) - 44.7
        print(f'\nO seu peso ideal é: {formula:.2f}')
    case _:
        print('\n### E.R.R.O.R ###')
