import os
os.system('cls')

soma = 0
materias = 0

while True:
    nota = float(input('Digite uma nota: '))
    soma = nota + soma
    resposta = input('Deseja adicionar mais um Nota? S pra Sim e N pra Não').upper()
    if resposta == 'N':
        materias += 1
        break
    elif resposta == 'S':
        materias += 1
    else:
        print('Resposta invalida')

media = soma / materias

print(f'{materias} {media}')