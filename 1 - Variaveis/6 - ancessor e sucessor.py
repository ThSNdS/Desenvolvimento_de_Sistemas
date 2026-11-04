import os
os.system("cls")

print('= SOLICITANDO DADOS =')
unidade_numerica = int(input('Digite uma unidade numérica de preferência: '))

antecessor = unidade_numerica - 1
sucessor = unidade_numerica + 1

print('\n= EXIBINDO DADOS =')
print('O antecessor do seu número é: ',antecessor)
print('O seu número é: ',unidade_numerica)
print('O sucessor do seu número é: ',sucessor)