import os
os.system('cls')

vetor_numero = []

for i in range(5):
    numero = int(input('Digite um número: '))
    if numero > 0:
        vetor_numero.append(numero)
    else:
        vetor_numero.append(0)

for numeros in vetor_numero:
    print(f'Números: {numeros}')