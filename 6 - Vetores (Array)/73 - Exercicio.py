import os
os.system('cls')

print('= INSERINDO NÚMEORS NO VETOR =')
vetor_numeros = []

for i in range(3):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)


print('\n= EXIBINDO NÚMEROS DO VETOR =')

for i in range(3):
    print(f'Valores: {vetor_numeros[i]}')


# SUA VEZ, MOSTRE A ÚLTIMA POSIÇÃO DO VETOR.