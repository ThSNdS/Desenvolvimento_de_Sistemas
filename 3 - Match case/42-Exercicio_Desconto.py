import os
os.system("cls")

produto = input('Digite o nome do produto que deseja comprar: ')
quantidade = int(input('Quantos dele: '))
preco = float(input('E o valor deles: '))

preco_total = quantidade * preco

if quantidade <= 5:
    desconto = preco_total * 0.02
elif quantidade > 5:
    desconto = preco_total * 0.03
elif quantidade > 10:
    desconto = preco_total * 0.05

preco_final = preco_total - desconto

print(preco_final)