import os
os.system("cls")

num = int(input('Digite uma número: '))
mun = int(input('digite outro número: '))

print(f" Os números são {num} e {mun}")
if num > mun:
    print(f'O maior é {num} e menor {mun}.')
else:
    print(f'O maior é {mun} e menor {num}.')