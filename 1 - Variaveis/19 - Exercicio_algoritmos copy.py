import os
os.system("cls")

num = int(input('Digite uma número: '))
mun = int(input('digite outro número: '))
nun = int(input('digite mais outro número: '))

maior = max(num, mun, nun)
menor = min(mun, num, nun)

print(f" Os números são {num}, {mun} e {nun}")
print('O maior é: ',maior)
print('O menor é: ',menor)