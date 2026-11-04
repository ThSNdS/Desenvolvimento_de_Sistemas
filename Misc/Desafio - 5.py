import os
os.system('cls')

vetor_notas = []
materias = 5
soma = 0
Acima = 0
for i in range(materias):
    nota = int(input('Digite sua nota: '))
    vetor_notas.append(nota)
    soma += nota
    media = soma / materias

for i in range(5):
    if vetor_notas[i] > media:
        Acima += 1

for i in range(5):
    print(f'Notas: {vetor_notas[i]}')

print(f'media: {media}')
print(f'Números de alunos acima da media: {Acima}')