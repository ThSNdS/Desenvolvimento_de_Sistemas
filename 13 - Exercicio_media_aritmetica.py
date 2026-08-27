import os
os.system("cls")

# ENTRADA
print('= SOLICITANDO DADOS =')
id= str(input('Escreva seu Nome: '))
nn1 = float(input('Digite sua nota de Lógica de Programação: '))
nn2 = float(input('Digite a nota de Fundamentos de Eletroeletrônica Aplicada: '))
nn3 = float(input('Digite a nota de Criatividade e ideação em projetos: '))

m21 = nn1 + nn2 + nn3
m22 = m21 / 3

print('\n= EXIBINDO DADOS =')
print('Seu nome é: ',id)
print('Suas notas são: ',nn1,nn2,nn3)

if m22 < 7:
    print('Calculando a a Média Aritmética: ',m22,('\n Você foi reprovado'))

else:
    print('Calculando a a Média Aritmética: ',m22,('\n Você foi aprovado'))