import os
os.system("cls")

# ENTRADA
print('= SOLICITANDO DADOS =')
identificacao= str(input('Escreva seu Nome: '))
salario = float(input('Digite seu Salário: '))

Economia = salario / 1621.00

print('\n= EXIBINDO DADOS =')
print('Seu nome é: ',identificacao)
print('Seu salário é: ',salario)
print('O Salário de:',salario, " Equivale a", Economia, 'Salários Mínimos.' )
