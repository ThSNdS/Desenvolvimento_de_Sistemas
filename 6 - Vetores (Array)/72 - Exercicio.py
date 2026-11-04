import os
os.system('cls')

print('= INSERINDO NÚMEORS NO VETOR =')
vetor_numeros = []

numero = int(input('Digite um número: '))
vetor_numeros.append(numero)
numero = int(input('Digite um número: '))
vetor_numeros.append(numero)
numero = int(input('Digite um número: '))
vetor_numeros.append(numero)

print('\n= EXIBINDO NÚMEROS DO VETOR =')
print(f'Primeira posição do vetor: {vetor_numeros[0]}')
print(f'Ùltima posição do vetor: {vetor_numeros[2]}')

# SUA VEZ, MOSTRE A ÚLTIMA POSIÇÃO DO VETOR.