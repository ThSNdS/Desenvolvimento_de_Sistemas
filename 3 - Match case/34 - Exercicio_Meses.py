import os
os.system("cls")

dia = int(input('Digite um dia: '))
mes = int(input('Digite um mes: '))
if dia > 31:
    print('Dia inválido')
elif dia > 29 and mes == 2:
    print('Data inválida')
else:
    match mes:
        case 1:
            nome = 'Janeiro'
        case 2:
            nome = 'Fevereiro'
        case 3:
            nome = 'Março'
        case 4:
            nome = 'Abril'
        case 5:
            nome = 'Maio'
        case 6:
            nome = 'Junho'
        case 7:
            nome = 'Julho'
        case 8:
            nome = 'Agosto'
        case 9:
            nome = 'Setembro'
        case 10:
            nome = 'Outubro'
        case 11:
            nome = 'Novembro'
        case 12:
            nome = 'Dezembro'
        case _:
            print('Mês inválido.')
    print(f'A data escolida foi dia {dia} de {nome}')