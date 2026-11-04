import os
os.system('cls')

soma = 0
materia = 2


for I in range(materia):
    while True:
        nota1 = float(input(f'Digite a nota da {I+1}º materia: '))
        if nota1 < 0 or nota1 > 10:
            print('\nNúmero invalido.')
        else:
            soma = soma + nota1
            break

media = soma / materia

print(f'\nA media é {media}.')