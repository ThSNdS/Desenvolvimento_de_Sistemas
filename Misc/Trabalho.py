import os

lista_prato = ['Picanha','Lasanha','Strogonoff', 'Bife Acebolado', 'Pão com Ovo']
lista_valor = [25.00, 20.00, 18.00, 15.00, 5.00]
lista_pedido = []

while True:
    os.system('cls')
    print('''
Menu
Código|     Prato      | Valor
   1  | Picanha        | 25,00
   2  | Lasanha        | 20,00
   3  | Strogonoff     | 18,00
   4  | Bife Acebolado | 15,00
   5  | Pão com Ovo    |  5,00
''')
    codigo = int(input('Digite o Código do prato que deseja: '))
    if codigo > 5 :
        print('Codigo invalido') 
    elif not type(codigo) is int:
        raise TypeError('Codigo invalido')
    else:
        lista_pedido.append(codigo)
        resposta = input('Deseja outro prato? (S/N): ').lower()
        if resposta == 'n':
            break