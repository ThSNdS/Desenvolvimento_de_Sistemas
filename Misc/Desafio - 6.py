import os
os.system('cls')

vetor_A = []
vetor_B = []
vetor_C = []
soma = 0

for i in range (5):
    numero_A = int(input('Digite um numero: ')  )
    vetor_A.append(numero_A)
    numero_B = int(input('Digite outro numero: ')  )
    vetor_B.append(numero_B)
    soma = numero_A + numero_B
    vetor_C.append(soma)

for valor in range(5):
    print(f'\nOs número são:A = {vetor_A[valor]} {vetor_B[valor]} {vetor_C[valor]}')