import os
os.system("cls")

cart = str(input('Digite seu nome: '))
idad = int(input('Digite sua idade: '))
max = 65
min = 16

if idad < min:
    print('Menor de idade não elegível ao voto')
elif idad <= 17:
    print('Voto opcional por menoridade')
elif idad > max:
    print('Voto opcional por maioridade')
else:
    print('Voto obrigatório')