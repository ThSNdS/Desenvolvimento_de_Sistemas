import os
from datetime import date
os.system('cls')

def nascimento():
    data = date.today().year - ano
    return data


dia = int(input('Digite o dia que voce nasceu: '))
mes = int(input('Digite o mês que voce nasceu: '))
ano = int(input('Digite o ano que voce nasceu: '))

total = nascimento()

print(f'\nVocê nasceu no dia {dia} mês {mes} no ano de {ano} a {total} anos atrás')