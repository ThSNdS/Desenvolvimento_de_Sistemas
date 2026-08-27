import os
os.system("cls")

# ENTRADA
print('= SOLICITANDO DADOS =')
primeira_unidade_numerica = float(input('Digite uma unidade numérica de preferência: '))
segunda_unidade_numerica = float(input('Digite outra unidade numérica: '))

# PROCESSAMENTO
soma = primeira_unidade_numerica + segunda_unidade_numerica
subtracao = primeira_unidade_numerica - segunda_unidade_numerica
multiplicacao = primeira_unidade_numerica * segunda_unidade_numerica
media = soma / 2

# SAÍDA
print('\n= EXIBINDO DADOS =')
print('\nSeus numero são: ', primeira_unidade_numerica, segunda_unidade_numerica)
print('\nA Media dos números é: ', media)
print('\nA Soma dos números é: ', soma)
print('\nA Produto dos números é: ', multiplicacao)
if primeira_unidade_numerica > segunda_unidade_numerica:
    print('\nO Maior dos números é: ', primeira_unidade_numerica)
else:
    print('\nA Maior dos números é: ', segunda_unidade_numerica)
