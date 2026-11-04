import os
os.system

vetor_numeros = []

for i in range(5):
    numero = int(input('Digite um número: '))
    vetor_numeros.append(numero)

menor = min(vetor_numeros)
maior = max(vetor_numeros)

print(f'O menor número é {menor} e o maior é {maior}')