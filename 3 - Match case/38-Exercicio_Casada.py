import os
os.system("cls")

print("#### SOLICITANDO DADOS ####")
nome = str(input('Digite seu nome: '))
sexo = str(input('Digite seu sexo: ')).upper()
estado_civil = str(input('Digite seu estado_civil: ')).lower()

if sexo == 'F' and estado_civil == 'casada':
    tempo = int(input('Digite seu tempo de casamento: '))
    print(f'''As suas informações são:
Nome = {nome}
Sexo = {sexo}
Estado civil = {estado_civil}
tempo casada = {tempo}
''')
else:
    print(f'''As suas informações são:
    Nome = {nome}
    Sexo = {sexo}
    Estado civil = {estado_civil}''')