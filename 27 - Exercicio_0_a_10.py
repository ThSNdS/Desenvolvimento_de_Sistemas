import os
os.system("cls")

nota = float(input('Digite a nota recebida: '))

if nota <= 0 or nota >= 10:
    print('A nota deve estar entre 0 e 10')
else:
    print(F'{nota}')