import os
os.system('cls')

vetor_numeros = []

for I in range(6):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)


print(f'Números antes: {vetor_numeros}')


for i in range(6):
    if vetor_numeros[i] % 2 == 0:
        vetor_numeros[i] = 0
    else:
        vetor_numeros[i] = 1

print(f'Números depois: {vetor_numeros}')