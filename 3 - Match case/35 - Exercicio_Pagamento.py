import os
os.system("cls")

preco = float(input('Digite o preço da compra: '))
pagamento = int(input('''Escolha a forma de pagamento
1 = Pagamento à vista
2 = Pagamento à prazo
Aperte o número indicado para realizar o pagamento: '''))

if pagamento == 1:
    forma = 'Vista'
    bonus = 'Desconto'
    bonus_total = '10%'
    valor = preco * 0.1
    valor_final = preco - valor
    print(f'\nVocê ira pagar {forma} tendo direito a {bonus} de {bonus_total} igual {valor}, no total {valor_final}')
elif pagamento == 2:
    forma = 'Prazo'
    bonus = 'Parcelas'
    bonus_total = int(input('Qual o número de parcelas que deseja: '))
    match bonus_total:
        case 1:
            valor = preco / 1
        case 2:
            valor = preco / 2
        case 3:
            valor = preco / 3
        case 4:
            valor = preco / 4
        case 5:
            valor = preco / 5
        case 6:
            valor = preco / 6
        case _:
            print('Número de parcelas inválido')
    valor_final = preco
    print(f'\nVocê ira pagar {forma} tendo direito a {bonus} de {bonus_total} igual {valor}, no total {valor_final}')
else:
    print('\nMétodo de pagamento inválido')