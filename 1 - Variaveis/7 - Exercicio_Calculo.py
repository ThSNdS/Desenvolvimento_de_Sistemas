import os
os.system("cls")

# ENTRADA
print('= SOLICITANDO DADOS =')
primeira_unidade_numerica = int(input('Digite uma unidade numérica de preferência: '))
segunda_unidade_numerica = int(input('Digite outra unidade numérica: '))

# PROCESSAMENTO
soma = primeira_unidade_numerica + segunda_unidade_numerica
subtracao = primeira_unidade_numerica - segunda_unidade_numerica
multiplicacao = primeira_unidade_numerica * segunda_unidade_numerica
divisao = primeira_unidade_numerica / segunda_unidade_numerica

# SAÍDA
print('\n= EXIBINDO DADOS =')
print('Seus numero são: ', primeira_unidade_numerica, segunda_unidade_numerica)
print('A Soma dos números é: ', soma)
print('A Multiplicação dos números é: ', multiplicacao)
print('A Divisão dos números é: ', divisao)