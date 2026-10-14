import os
os.system

nomes = []

for i in range (5):
    livros = input('Escreva o nome do livro: ')
    nomes.append(livros)

for i in range (5):
    print(f'Livros: {nomes[i]}')