import os
os.system('cls')

notas =  0

for escola in range (1,5):
    notas += float(input(f'Digite {escola}º nota:'))

media = notas / escola

if media >= 7:
    print(f'Sua media foi {media} e você foi aprovado.')
elif media >= 4:
    print(f'Sua media foi {media} e você devera fazer recuperação.')
else:
    print(f'Sua media foi {media} e você foi reprovado.')
