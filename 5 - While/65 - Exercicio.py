import os
os.system('cls')

soma = 0
materias = 0
notas = 0

while True:
    resposta = input('Deseja adicionar mais um Nota? S pra Sim e N pra Não').upper()
    if resposta == 'N':
        materias += 1
        break
    elif resposta == 'S':
        nota = float(input('Digite uma nota: '))
        notas += 1
        materias += 1
    else:
        print('Resposta invalida')

if notas == 0:
    print('Nenhuma Nota presentada.')
else:
    soma = nota + soma
    media = soma / materias
    print(f'{materias} {media}')