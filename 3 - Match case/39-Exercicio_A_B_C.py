import os
os.system('cls')

a1 = int(input('Digite um numero: '))
b1 = int(input('Digite outro numero: '))

if a1 == b1:
    c1 = a1 + b1
else:
    c1 = a1 * b1

print(f'\nA = {a1}, B = {b1} e C = {c1}')