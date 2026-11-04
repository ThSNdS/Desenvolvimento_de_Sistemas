import os
os.system('cls')

vetor_nomes = []
vetor_salario = []
maior_salario = None
maior_nome = ''
contagem = 0

for I in range(5):
    nome = input('Escreva seu nome: ')
    vetor_nomes.append(nome)
    salario = float(input('Digite seu salario: '))
    if salario > 2000.00:
        contagem += 1
    vetor_salario.append(salario)
    salarios = salario
    if maior_salario is None or salarios > maior_salario:
        maior_salario = salarios
        maior_nome = nome

print(f'\nExiste {contagem} fucionarios que ganha mais de 2000.00, mas o que possui o maior é {maior_nome} que recebe {maior_salario}.')