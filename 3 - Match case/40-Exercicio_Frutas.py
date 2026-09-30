import os
os.system('cls')

print('''As suas informações são:
Fruta   |    Até 5 Kg    | Acima de 5 Kg
Morango | R$ 2,50 por Kg | R$ 2,20 por Kg
Maça    | R$ 1,80 por Kg | R$ 1,50 por Kg
''')

morango = float(input('\nDigite quantos kilos de morango deseja pagar: '))
maça = float(input('Digite quantos kilos de maça deseja pagar: '))

if morango < 6:
    valor1 = morango * 2.50
else:
    valor1 = morango * 2.20

if maça < 6:
    valor2 = maça * 1.80
else:
    valor2 = maça * 1.50

valor_total = valor1 + valor2
kg_total = morango + maça
desconto = (valor1 + valor2) * 0.1
valor_final = valor_total

if valor_total > 15.00 or kg_total >= 10:
    valor_final = valor_total - desconto

print(f'Preço total das compras:{valor_total:.2f}')