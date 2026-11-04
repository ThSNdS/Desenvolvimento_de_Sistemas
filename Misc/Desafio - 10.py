import os
os.system('cls')

vetor_idade = []
idosos = 5
maior_idade = 0
for i in range(5):
    idade = int(input('Digite sua idade: '))
    while idade < 0 or idade > 120:
        print("Idade inválida! Digite um valor entre 0 e 120.")
        idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    vetor_idade.append(idade)
    if idade > 18:
        maior_idade += 1

maior = max(vetor_idade)
menor = min(vetor_idade)

print(f'A pessoa mais velha possui {maior} e a mais nova {menor}, existem {maior_idade} maiores de idade.')