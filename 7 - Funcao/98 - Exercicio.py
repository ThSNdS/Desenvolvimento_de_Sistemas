import os
os.system('cls')

notas = []

def calculo_media():
    total = sum(notas) / len(notas)
    return total

for i in range(3):
    nota = float(input(f'Digite a {i+1}º nota: '))
    notas.append(nota)

media = calculo_media()

print(f'\nSua média foi {media}')