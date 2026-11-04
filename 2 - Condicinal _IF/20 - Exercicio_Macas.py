import os
os.system("cls")

# ENTRADA.
maca = int(input('Digite o número de maçãs que deseja comprar: '))

# PROCESSAMENTO.
if maca >= 12:
    preco = 1.00
else:
    preco = 1.30

valor = preco * maca

# SAÍDA.
print(F'\nO valor das compras deram {valor:.2f}')