import os
import time
os.system('cls')

numero = int(input('Digite um número: '))

for I in range (numero,0,-1):
    print(f'{I}')
    time.sleep(1)

print('FIM')