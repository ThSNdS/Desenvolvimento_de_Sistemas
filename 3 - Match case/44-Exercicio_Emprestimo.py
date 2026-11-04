import os
os.system('cls')

renda = float(input('Digite sua renda mensal: '))

emprestimo_max = renda * 10
prestacao_max = renda * 0.3

emprestimo = float(input('Quanto de emprestimo deseja: '))
if emprestimo > emprestimo_max:
    print(f'Valor do emprestimo inviavel, {emprestimo_max} é limite.')
else:
    prestacoes = int(input('Numero de prestações: '))
    prestacao = emprestimo / prestacoes
    if prestacao > prestacao_max:
        print(f'Valor do prestaçao inviavel, {prestacao_max} é limite.')
    else:
        print(f"\nemprestimo aceito no valor de {emprestimo:.2f} pago em {prestacoes:.2f} vezes de {prestacao:.2f}")

