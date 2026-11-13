import os
os.system('cls')

#Função com parâmetros e com retorno
def calcular_notas(nota1, nota2):
    resultado = (nota1 + nota2) / 2
    return resultado

def verificar_resultado(media):
    if media >= 7.0:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'
    return situacao

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#Usando uma função com parâmetros e
#Inserindo o retorno na variável soma.
media = calcular_notas(nota1, nota2)
final = verificar_resultado(media)

print('= EXIBINDO NOTAS =')
print(f'Média: {media}')
print(f'Resultado: {final}')
