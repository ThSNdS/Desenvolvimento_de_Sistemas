import os
os.system('cls')

vetor_numeros = []
pares = 0
impares = 0

for indice in range(6):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)

for numero in range(6):
    print(f'Número: {numero}')
    if numero % 2 == 0:
        print('É par')
        pares += 1
    else:
        print('É impar')
        impares += 1

print(f'Foram {pares} números pares e {impares} impares.')