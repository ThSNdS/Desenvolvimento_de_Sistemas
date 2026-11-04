import os
os.system("cls")

# ENTRADA.
nome = str(input('Escreva seu nome: '))
peso = float(input('Digite teu peso: '))
altura = float(input('Coloque aqui sua altura: '))

# PROCESSAMENTO.
mxm = altura * altura
imc = peso / mxm

if imc <= 18.5:
    clasf = 'Abaixo do peso'
elif imc <= 24.9:
    clasf = 'Peso ideal'
elif imc <= 29.9:
    clasf = 'Levemente acima do peso' 
elif imc <= 34.9:
    clasf = 'Obesidade grau 1'
elif imc <= 39.9:
    clasf = 'Obesidade grau 2'
else:
    clasf = 'Obesidade grau 3'

# SAÍDA.
print('Nome: ',nome)
print('altura: ',altura)
print('Peso: ',peso)
print(F'I.M.C-Índice de Massa Corporal: {imc:.2f}')
print('Classifacação: ',clasf)

if clasf == 'Peso ideal':
    print('*** PARABÉNS ***')
elif clasf == 'Obesidade grau 2':
    print("**** Atenção Obesidade Severa ****")
elif clasf == 'Obesidade grau 3':
    print("**** Atenção Obesidade Mórbida ****")