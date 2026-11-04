import os
os.system('cls')


while True:
    nota = float(input('Escreva sua nota: '))
    if nota < 0 or nota > 10:
        print(f'O número {nota} é invalido.')
    else:
        print(f'\n{nota}.')
        break
