import os
os.system('cls')

soma = 0
mulheres = 0
grupo = 0

while True:
    codigo = input(''' Digite o código com a opção desejada:
    Código  Descrição
    1     | Adicionar pessoa
    2     | Exibir resultados
    3     | Sair
    ''')
    match codigo:
        case '1':
            grupo += 1
            print('pra adicionar uma pessoa é preciso a entrega de certos dados.')
            nome = input('Escreva seu nome: ')
            idade = int(input('Escreva sua idade: '))
            vida = idade
            maior = None
            menor = None
            if maior is None:
                maior = vida
            if menor is None:
                menor = vida
            if vida > maior:
                maior = vida
            if vida < menor:
                menor = vida
            sexo = input('Escreva seu sexo(M/F): ').upper()
            salario = float(input('Escreva seu salário: '))
            soma += salario
            if sexo != 'M' and sexo != 'F':
                print('Sexo invalido')
            elif sexo == 'F' and salario > 5000:
                mulheres += 1
            os.system('cls')
        case '2':
            media = soma / grupo
            print(f'\n A média de salário do grupo é {media}')
            print(f'\n O mais velho/velha do grupo possui {maior} já a mais nova/novo {menor}')
            print(f'\n Existem {mulheres} Mulheres com salário de mais que 5000.00')
        case '3':
            break
        case _:
            print('Código invalido')
