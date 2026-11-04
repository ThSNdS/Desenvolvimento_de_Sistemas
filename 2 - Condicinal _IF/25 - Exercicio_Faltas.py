import os
os.system("cls")

nome = str(input('Digite seu nome: '))
print(F'Então {nome} Responda')
media = float(input('Qual é sua média: '))
faltas = int(input('Quantas faltas você possui: '))

media_aprovada = float (7.0)
faltas_limtes = 40

if media < media_aprovada or faltas> faltas_limtes:
    print(F'Aluno:{nome}, Você foi reprovado')
else:
    print(F'Aluno:{nome}, Você foi aprovado')