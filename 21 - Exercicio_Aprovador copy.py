import os
os.system("cls")

# ENTRADA.
nota1 = float(input('Digite a nota da materia: '))
nota2 = float(input('Digite sua nota de displina: '))

# PROCESSAMENTO.
total = nota1 + nota2
media = total / 2

# SAÍDA.
if media >= 9:
    print(F'Sua média foi de {media} isso equivale a A.\n Você foi Aprovado ')
elif media >= 7.5 < 9:
    print(F'Sua média foi de {media} isso equivale a B.\n Você foi Aprovado ')
elif media >= 6 < 7.5:
    print(F'Sua média foi de {media} isso equivale a C.\n Você foi Aprovado ')
elif media >= 4 < 6:
    print(F'Sua média foi de {media} isso equivale a D.\n Você foi Reprovado ')
elif media < 4:
    print(F'Sua média foi de {media} isso equivale a E.\n Você foi Reprovado ')