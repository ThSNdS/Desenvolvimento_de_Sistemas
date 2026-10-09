import os
import time
os.system

familias = 0
soma_salario = 0
soma_filho = 0
maior = 0
menor = 0

while True:
    codigo = input(''' Digite o código com a opção desejada:
    Código  Descrição
    1     | Adicionar família
    2     | Exibir resultados e sair
    ''')
    match codigo:
        case '1':
            familias += 1
            salario = float(input('Digite seu sálario: '))
            soma_salario += salario
            if maior == 0 or salario > maior:
                maior = salario
            if menor == 0 or salario < menor:
                menor = salario
            filhos = int(input('Escreve o número de filhos que sua possui: '))
            soma_filho += filhos
        case '2':
            if familias > 0:
                media_filhos = soma_filho/ familias 
                media_salario = soma_salario / familias 
                print(f'Total de família: {familias}')
                print(f'Média do salário da população: {media_salario}')
                print(f'Média de filhos da população: {media_filhos}')
                print(f'O maior sálario: {maior}')
                print(f'O menor sálario: {menor}')
                time.sleep(5)
                break
            else:
                print('\nFalta de dados pra exibição.')
        case _:
            print('Código invalido')

