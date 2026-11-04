import os
os.system('cls')

vetor_numeros = []
negativos = 0
soma  = 0

for indice in range(5):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)
    if numero < 0:
        negativos += 1
    else:
        soma += numero

print(f'\nExiste {negativos} números negativos e a soma dos positivos é {soma}')