import os
os.system('cls')

soma = 0

print(f'Valor da variável soma: {soma}')

for i in range(3):
    numero = int(input('Digite um número para somar: '))
    soma = soma + numero
    print(f'valor temporário da variavél soma: {soma}')

print(f'Valor FINAL da variavél soma: {soma}')