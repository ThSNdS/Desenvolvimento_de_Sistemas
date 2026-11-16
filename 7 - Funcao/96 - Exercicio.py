import os
os.system('cls')

def inflacao(preco):
    if preco < 100:
        aumento = preco * 1.1
    else:
        aumento = preco * 1.2
    return aumento


preco = float(input('Digite o preço do produto: '))

pagemento = inflacao(preco)

print(f'\nO valor ser pago é {pagemento:.2f}')