import os
os.system("cls")

print('Quando pedido escreva o numero que deseja pra ser vinculado a cada letra')
ac = int(input("Digite o numero que deseja pra A: "))
ba = int(input("Digite o numero que deseja pra B: "))
cb = int(input("Digite o numero que deseja pra C: "))

soma = ac + ba

if soma > cb:
    print(f'A junção de A e B é maior que C.')
else:
    print(f'A junção de A e B é menor que C')