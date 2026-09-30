import os
os.system("cls")

# ENTRADA
print('= SOLICITANDO DADOS =')
id= str(input('Escreva seu Nome: '))
nota1 = float(input('Digite sua nota de Lógica de Programação: '))
nota2 = float(input('Digite a nota de Fundamentos de Eletroeletrônica Aplicada: '))


media1 = nota1 + nota2
media2 = media1 / 2

if media2 >= 4.1 and media2 <= 5.9:
    print('Calculando a a Média Aritmética: ',media2,('\n Você está viavel a recuperação.'))
elif media2 >= 6:
    print('Calculando a a Média Aritmética: ',media2,('\n Você foi aprovado.'))
else:
    print('Calculando a a Média Aritmética: ',media2,('\n Você foi reprovado.'))