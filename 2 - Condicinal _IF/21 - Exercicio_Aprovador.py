import os
os.system("cls")

# ENTRADA.
nota1 = float(input('Digite a nota da materia: '))
nota2 = float(input('Digite sua nota de displina: '))

# PROCESSAMENTO.
total = nota1 + nota2
media = total / 2
letra = 'F'
estado = 'Cprovado'

if media > 9:
    letra = 'A' 
    estado = 'Aprovado'
elif media >= 7.5 < 9:
    letra = 'B' 
    estado = 'Aprovado'
elif media >= 6 < 7.5:
    letra = 'C' 
    estado = 'Aprovado'
elif media >= 4 < 6:
    letra = 'D' 
    estado = 'Reprovado'
elif media <= 4:
    letra = 'E' 
    estado = 'Reprovado'

print(F'Sua média foi de {media} isso equivale a um {letra}.\n Você foi {estado} ')