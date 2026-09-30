import os
from datetime import date
os.system("cls")

# ENTRADA.
codig = int(input('Digite o código da empresa: '))
nasc= int(input('Escreva o ano do seu nascimento: '))
traba = int(input('Coloque aqui o tempo de trabalho que possui, em anos: '))

# PROCESSAMENTO.
if codig == 123456:
    print('Código aceito, prosseguir.')
else:
    import sys
    sys.exit("Código inválido")

idade = date.today().year - nasc

# SAÍDA
if traba <= 30 or idade <= 65:
    print('\nPropenso a requesição da aposentadoria')
else:
    print('\nNão possui direto a requesitar a aposentadoria')



