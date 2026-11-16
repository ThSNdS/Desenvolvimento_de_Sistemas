import os
os.system('cls')

notas = []

def calculo_media():
    total = sum(notas) / len(notas)
    print(f'\nSuas notas são {notas} e a média {total}')

for i in range(3):
    nota = float(input(f'Digite a {i+1}º nota: '))
    notas.append(nota)

calculo_media()