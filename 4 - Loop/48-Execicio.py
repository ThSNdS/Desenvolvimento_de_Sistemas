import os
os.system('cls')

soma = 0
for i in range (1,6):
    numero = int(input(f'Digite {i}º número número: '))
    soma += numero

print(soma)