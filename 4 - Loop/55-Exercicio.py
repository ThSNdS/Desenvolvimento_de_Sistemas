import os
os.system('cls')

pares = 0
impares = 0
for varivel in range(5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        print(f'O número {numero} é par')
        pares += 1
    else:
        print(f'O número {numero} é ímpar')
        impares += 1

print(f'Existe {pares} número pares e {impares} número ímpares.')