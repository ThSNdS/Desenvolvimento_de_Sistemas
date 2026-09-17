import os
os.system('cls')

print('!!!! Atenção A = Àlcool G = Gasolina !!!!')
tipo = input('Escolha seu tipo de combustível: ').upper()
litros = float(input('Quantos litros: '))

match tipo:
    case 'A':
        preço = 3.79
        if litros <= 25:
            desconto = 0.1
        else:
            desconto = 0.2
    case 'G':
        preço = 6.59
        if litros <= 25:
            desconto = 0.15
        else:
            desconto = 0.3



preço_total = preço * litros
desconto_real = preço_total * desconto
preço_real = preço_total - desconto_real

print(f'{preço_real:.2f}')