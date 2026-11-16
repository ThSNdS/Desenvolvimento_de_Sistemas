import os
os.system('cls')

materias = 2
soma = 0
def nota_correta():
    print('A nota deve estar entre 0 e 10.')
def calculado_media():
    valor = soma / materias
    return valor
def resultado():
    if media >= 7.0:
        estado = 'Aprovado'
    else:
        estado = 'Reprovado'
    return estado

for I in range(materias):
    while True:
        nota1 = float(input(f'Digite a nota da {I+1}º materia: '))
        if nota1 >= 0 and nota1 <= 10:
            soma += nota1
            break
        else:
            nota_correta()

media = calculado_media()
situacao = resultado()

print(f'\n {media} {situacao}')
