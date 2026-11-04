import os
os.system('cls')

notas = []
soma = 0
for i in range(4):
    valor = float(input(f'Digite sua nota da {i+1}º Materia: '))
    notas.append(valor)


media = sum(notas) / 4
if media >= 7:
    resultado = 'Aprovado'
elif media >= 5:
    resultado = 'Recuperação'
elif media < 5:
    resultado = 'Reprovado'

for posicao, valor in enumerate(notas ,start=1):
    print(f'Nota da {posicao}º Materia : {valor}')
print(f'Sua media é: {media}, Você está {resultado}')