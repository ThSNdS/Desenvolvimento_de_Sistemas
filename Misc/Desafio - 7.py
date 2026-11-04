import os
os.system('cls')

vetor_1 = []
vetor_2 = []
elementos = 0

for i in range(10):
    numero = int(input('Digite um número: '))
    vetor_1.append(numero)
    if numero > 0:
        vetor_2.append(numero)
        elementos += 1

print(f'\nForam adqueridos {elementos} números.')
print(f'Números: {vetor_2}')