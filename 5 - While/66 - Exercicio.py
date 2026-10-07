import os
os.system('cls')

vezes = 0
soma = 0
while True:
    algoritmo = int(input('Digite um número: '))
    if algoritmo < 0:
        break
    else:
        vezes += 1
        soma += algoritmo

media = soma / vezes

print(f'\n{media} {soma} {vezes}')