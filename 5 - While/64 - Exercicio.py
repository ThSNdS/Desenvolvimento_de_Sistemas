import os
os.system('cls')

soma = 0
materia = 3


for I in range(materia):
    while True:
        nota1 = float(input(f'Digite a nota da {I+1}º materia: '))
        if nota1 < 0 or nota1 > 10:
            print('\nNúmero invalido.')
        else:
            soma = soma + nota1
            break

media = soma / materia

if media >= 7:
    Resultado = 'Aprovado'
    Resultado = 'Aprovado'
elif media >= 5 and media <= 6.9:
    Resultado = 'Em Recuperação'
else:
    Resultado = 'Reprovado'

print(f'\nA media é {media}.')
print(f'\nO aluno está {Resultado}.')