import os
os.system('cls')

numero = int(input('Digite um número: '))

impares = 0
impar = 0
pares = 0
par_total = 0
soma = 0

for i in range (numero,0,-1):
    print(f'{i}')
    soma += i
    if i % 2 != 0:
        impares += 1
        impar = impar + i
    else:
        pares = pares + 1
        par_total += i

media_par = par_total / pares
media = soma / numero

print(f'\n{pares} {impares} {media_par} {media}')